import numpy as np
import random

import distance
import main

def run(a, b, dist_table):

    n_cities = 51
    current_order = [i for i in range(1, n_cities + 1)]
    current_score = distance.calc_path_length(current_order, dist_table)
    
    orders = [current_order]
    scores = [current_score]

    for i in range(1000):


        edge1 = random.randint(0, n_cities - 1)
        edge2 = random.randint(0, n_cities - 1)

        # TODO edge checks
        
        temp_order = main.two_opt(current_order, edge1, edge2)
        temp_score = distance.calc_path_length(temp_order, dist_table)

        temperature = calc_temp(a, b, i)
        if temp_score < current_score or is_excepted(temp_score, temperature):
            current_score = temp_score
            current_order = temp_order

        scores.append(current_score)
        orders.append(current_order)

    return scores, orders
       
def is_excepted(value, temperature):
    return random.random() < acceptance_change(value, temperature)     

def calc_temp(a, b, n):
    return a / np.log(n + b)

def acceptance_change(value, temperature):
    return np.exp(-value / temperature)