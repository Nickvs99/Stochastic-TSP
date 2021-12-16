def read_file(filename):
    x_list = []
    y_list = []

    with open(filename, "r") as f:
        print(filename)
        for line in f.readlines()[6:-1]:
            split_line = line.split(' ')
            split_line = [x for x in split_line if x]
            x_list.append(float(split_line[-2]))
            y_list.append(float(split_line[-1]))

    return x_list, y_list

def read_solution(filename):
    node_list = []

    with open(filename, "r") as f:
        print(filename[-17:])
        if filename[-17:] == 'a280.opt.tour.txt':
            for line in f.readlines()[4:-1]:
                node_list.append(int(line))
        else:
            for line in f.readlines()[5:-2]:
                node_list.append(int(line))

    node_list.append(node_list[0])
    return node_list

# Example usage
#print(read_solution('TSP-Configurations/eil51.opt.tour.txt'))