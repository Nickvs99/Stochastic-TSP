

def create_distance_table(x_values, y_values):
    """
    Creates a dictionary with the distance between node i and j.


    """

    distance_table = {}
    if len(x_values) != len(y_values):
        raise Exception(f"Dimensions of x_values and y_values should be the same. {len(x_values)} vs {len(y_values)}")

    for i in range(len(x_values)):
        for j in range(len(y_values)):

            temp_i = i + 1
            temp_j = j + 1

            if temp_i not in distance_table:
                distance_table[temp_i] = {}

            x1, x2 = x_values[i], x_values[j]
            y1, y2 = y_values[i], y_values[j]

            distance_table[temp_i][temp_j] = calc_distance(x1, y1, x2, y2)

    return distance_table
    
def calc_distance(x1, y1, x2, y2):

    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5