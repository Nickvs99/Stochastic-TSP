import numpy as np
import random

import distance
import main

def run(a, b, dist_table, iterations=10000, chain_length=1):
    temp_list = []
    n_cities = len(dist_table)
    current_order = [i for i in range(1, n_cities + 1)]
    current_order.append(1)
    current_score = distance.calc_path_length(current_order, dist_table)
    
    orders = [current_order]
    scores = [current_score]
    last_value = np.inf

    for i in range(iterations):


        edge1 = random.randint(0, n_cities - 1)
        edge2 = random.randint(0, n_cities - 1)

        while abs(edge1 - edge2) < 2:
            edge1 = random.randint(0, n_cities - 1)
            edge2 = random.randint(0, n_cities - 1)
        
        temp_order = main.two_opt(current_order, edge1, edge2)
        temp_score = distance.calc_path_length(temp_order, dist_table)

        if i % chain_length == 0:
            temperature = calc_temp(a, b, i/chain_length)
        temp_list.append(temperature)
        if temp_score < current_score or is_excepted(temp_score, last_value, temperature):
            current_score = temp_score
            current_order = temp_order

        scores.append(current_score)
        orders.append(current_order)

        last_value = current_score

    return scores, orders
       
def is_excepted(value, last_value, temperature):
    return random.random() < acceptance_change(value, last_value, temperature)     

def calc_temp(a, b, n):
    return a / np.log(n + b + 1)

def acceptance_change(value, last_value, temperature):
    return np.exp(-(value - last_value) / temperature)