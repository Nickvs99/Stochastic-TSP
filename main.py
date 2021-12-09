import random

import distance
import file_reader


def main():

    x_values, y_values = file_reader.read_file("TSP-Configurations/eil51.tsp.txt")

    dist_table = distance.create_distance_table(x_values, y_values)

    # TEMP, create a random order of cities
    city_order = [i for i in range(1, 52)]
    random.shuffle(city_order)

    path_length = distance.calc_path_length(city_order, dist_table)
    print(path_length)

if __name__ == "__main__":
    main()