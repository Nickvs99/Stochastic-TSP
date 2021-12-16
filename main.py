import random
import numpy as np
import matplotlib.pyplot as plt

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
    n = 1000000
    filename = 'eil51'
    x_values, y_values = read_file(f"TSP-Configurations/{filename}.tsp.txt")
    route = read_solution(f"TSP-Configurations/{filename}.opt.tour.txt")

    dist_table = distance.create_distance_table(x_values, y_values)

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
    
if __name__ == "__main__":
    main()