import random
import numpy as np

import distance
from file_reader import read_file, read_solution
from plot import plot


def two_opt(order, edge_1, edge_2):
    if edge_2 < edge_1:
        edge_1, edge_2 = edge_2, edge_1
    new_order = np.zeros(len(order))
    new_order[:edge_1] = order[:edge_1]
    new_order[edge_1:edge_2] = list(reversed(order[edge_1:edge_2]))
    new_order[edge_2:] = order[edge_2:]
    new_order = [int(i) for i in new_order]
    if edge_1 == 0:
        new_order[-1] = new_order[0]
    if edge_2 == len(new_order):
        new_order[0] = new_order[-1]
    print(new_order)
    return new_order


def main():
    filename = 'eil51'
    x_values, y_values = read_file(f"TSP-Configurations/{filename}.tsp.txt")

    dist_table = distance.create_distance_table(x_values, y_values)

    # TEMP, create a random order of cities
    city_order = [i for i in range(1, 52)]
    random.shuffle(city_order)
    city_order = read_solution(f"TSP-Configurations/{filename}.opt.tour.txt")
    city_order = two_opt(city_order, 10, 52)

    path_length = distance.calc_path_length(city_order, dist_table)
    print(path_length)

    plot(x_values, y_values, city_order)

if __name__ == "__main__":
    main()