def read_file(filename):
    x_list = []
    y_list = []

    with open(filename, "r") as f:
        for line in f.readlines()[6:-1]:
            split_line = line.split(' ')
            x_list.append(float(split_line[1]))
            y_list.append(float(split_line[2]))

    return x_list, y_list

# Example usage
# print(read_file('TSP-Configurations/pcb442.tsp.txt'))