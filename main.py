import random
import numpy as np

import distance
from file_reader import read_file, read_solution
from plot import plot, plot_scores
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


def main():
    filename = 'eil51'
    x_values, y_values = read_file(f"TSP-Configurations/{filename}.tsp.txt")

    dist_table = distance.create_distance_table(x_values, y_values)

    scores, orders = simulated_annealing.run(1000, 10, dist_table, iterations=1000000)

    index = scores.index(min(scores))
    optimal_route = orders[index]
    
    print(orders[index])
    print(scores[index]) 
    
    plot_scores(scores)
    plot(x_values, y_values, optimal_route)

if __name__ == "__main__":
    main()