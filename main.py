import random

import distance
from file_reader import read_file, read_solution
from plot import plot


def main():
    filename = 'eil51'
    x_values, y_values = read_file(f"TSP-Configurations/{filename}.tsp.txt")

    dist_table = distance.create_distance_table(x_values, y_values)

    # TEMP, create a random order of cities
    city_order = [i for i in range(1, 52)]
    random.shuffle(city_order)
    city_order = read_solution(f"TSP-Configurations/{filename}.opt.tour.txt")

    path_length = distance.calc_path_length(city_order, dist_table)
    print(path_length)

    plot(x_values, y_values, city_order)

if __name__ == "__main__":
    main()