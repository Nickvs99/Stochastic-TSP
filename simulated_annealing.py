import numpy as np
import random

import distance
import main

<<<<<<< HEAD
def run(a, b, n, dist_table):
    temp_list = []
=======
def run(a, b, dist_table, iterations=10000):

>>>>>>> d5b2df232220fbaca8466ce6253b96a1fd6382bc
    n_cities = len(dist_table)
    current_order = [i for i in range(1, n_cities + 1)]
    current_order.append(1)
    current_score = distance.calc_path_length(current_order, dist_table)
    print(current_score)
    
    orders = [current_order]
    scores = [current_score]
    last_value = np.inf

    for i in range(n-1):


        edge1 = random.randint(0, n_cities - 1)
        edge2 = random.randint(0, n_cities - 1)

        while abs(edge1 - edge2) < 2:
            edge1 = random.randint(0, n_cities - 1)
            edge2 = random.randint(0, n_cities - 1)
        
        temp_order = main.two_opt(current_order, edge1, edge2)
        temp_score = distance.calc_path_length(temp_order, dist_table)

        temperature = calc_temp(a, b, i)
        temp_list.append(temperature)
        if temp_score < current_score or is_excepted(temp_score, last_value, temperature):
            current_score = temp_score
            current_order = temp_order

        scores.append(current_score)
        orders.append(current_order)

        last_value = current_score

    return scores, orders, temp_list
       
def is_excepted(value, last_value, temperature):
    return random.random() < acceptance_change(value, last_value, temperature)     

def calc_temp(a, b, n):
    return a / np.log(n + b)

def acceptance_change(value, last_value, temperature):
    return np.exp(-(value - last_value) / temperature)