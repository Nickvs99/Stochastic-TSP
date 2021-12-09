import file_reader
import distance_table

def main():

    x_values, y_values = file_reader.read_file("TSP-Configurations/eil51.tsp.txt")

    dist_table = distance_table.create_distance_table(x_values, y_values)

    print(dist_table)
    
if __name__ == "__main__":
    main()