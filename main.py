import numpy as np
<<<<<<< HEAD
import matplotlib.pyplot as plt
=======
import os
import pickle
>>>>>>> d5b2df232220fbaca8466ce6253b96a1fd6382bc

import distance
from file_reader import read_file, read_solution
from plot import plot, plot_scores, plot_data
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

def generate_data(a_values, b_values, nruns, dist_table, iterations=10000):

    data = {}
    best_score = np.inf
    best_order = None
    
    for a in a_values:
        for b in b_values:
            print(f"\rCalculating a={a}, b={b}...", end="")
            score_results = []

            for _ in range(nruns):

                scores, orders = simulated_annealing.run(a, b, dist_table, iterations=iterations)
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
    n = 1000000
    filename = 'eil51'
    cache_filename = f"data/{filename}.pickle"
    
    x_values, y_values = read_file(f"TSP-Configurations/{filename}.tsp.txt")
<<<<<<< HEAD
    route = read_solution(f"TSP-Configurations/{filename}.opt.tour.txt")

=======
>>>>>>> d5b2df232220fbaca8466ce6253b96a1fd6382bc
    dist_table = distance.create_distance_table(x_values, y_values)
    
    if os.path.isfile(cache_filename):
        print(f"Loading cached data from {cache_filename}")
        data, best_score, best_order = load_data(cache_filename)
    else:
        print(f"Calculating cached data for {cache_filename}")

        a_values = [1, 10, 100, 1000, 10000]
        b_values = [1, 10, 100, 1000, 10000]
        data, best_score, best_order = generate_data(a_values, b_values, 25, dist_table)

<<<<<<< HEAD
    afstand = distance.calc_path_length(route, dist_table)
    print(afstand)
    scores, orders, temp_list = simulated_annealing.run(50, 20, n, dist_table)

    #plot(x_values, y_values, orders[0])
    print(min(scores))
    index = scores.index(min(scores))
    route = orders[index]
    plot(x_values, y_values, route)
    plt.plot(np.arange(n), scores)
    plt.show()
    plt.plot(np.arange(n-1), temp_list)
    plt.show()
=======
        print(f"Saving data to {cache_filename}")
        save_data(cache_filename, data, best_score, best_order)

    plot_data(data)
>>>>>>> d5b2df232220fbaca8466ce6253b96a1fd6382bc
    
    print(best_score)
    plot(x_values, y_values, best_order)

if __name__ == "__main__":
    main()