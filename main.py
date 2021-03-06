import numpy as np
import matplotlib.pyplot as plt
import os
import pickle

import distance
from file_reader import read_file, read_solution
from plot import plot, plot_scores, plot_data, plot_best_difference
import simulated_annealing


def two_opt(order, city_1, city_2):
    if city_2 < city_1:
        city_1, city_2 = city_2, city_1
    new_order = np.zeros(len(order))
    new_order[:city_1] = order[:city_1]
    new_order[city_1:city_2] = list(reversed(order[city_1:city_2]))
    new_order[city_2:] = order[city_2:]
    new_order = [int(i) for i in new_order]
    if city_1 == 0:
        new_order[-1] = new_order[0]
    if city_2 == len(new_order):
        new_order[0] = new_order[-1]
    return new_order

def generate_data(a_values, b_values, nruns, dist_table, iterations=10000, chain_length=1):

    data = {}
    best_score = np.inf
    best_order = None
    
    for a in a_values:
        for b in b_values:
            print(f"\rCalculating a={a}, b={b}...", end="", flush=True)
            score_results = []

            for _ in range(nruns):

                scores, orders = simulated_annealing.run(a, b, dist_table, iterations=iterations, chain_length=2)
                score_results.append(scores)

                min_score = min(scores)
                if min_score < best_score:
                    index = scores.index(min_score)
                    best_score = min_score
                    best_order = orders[index]

            if a not in data:
                data[a] = {}

            data[a][b] = score_results
    print()
    return data, best_score, best_order

def save_data(filename, data, best_score, best_order):
    with open(filename, 'wb') as f:
        pickle.dump([data, best_score, best_order], f)

def load_data(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def main():
    filename = 'eil51'
    cache_filename = f"data/{filename}.pickle"
    
    x_values, y_values = read_file(f"TSP-Configurations/{filename}.tsp.txt")
    optimal_order = read_solution(f"TSP-Configurations/{filename}.opt.tour.txt")

    dist_table = distance.create_distance_table(x_values, y_values)
    
    if os.path.isfile(cache_filename):
        print(f"Loading cached data from {cache_filename}")
        data, best_score, best_order = load_data(cache_filename)
    else:
        print(f"Calculating cached data for {cache_filename}")

        a_values = [0.01, 0.1, 1, 10, 100]
        b_values = [1, 10, 100, 1000, 100000]
        data, best_score, best_order = generate_data(a_values, b_values, 25, dist_table, chain_length=1, iterations=100000)

        print(f"Saving data to {cache_filename}")
        save_data(cache_filename, data, best_score, best_order)

    optimal_score = distance.calc_path_length(optimal_order, dist_table)
    print(optimal_score, best_score)
    
    plot_best_difference(data, optimal_score)
    plot_data(data)
    plot(x_values, y_values, optimal_order)

if __name__ == "__main__":
    main()