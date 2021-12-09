import matplotlib.pyplot as plt
import numpy as np

def plot(x_points, y_points, route=None):
    x = np.zeros(len(route))
    y = np.zeros(len(route))
    for i in range(len(route)):
        x[i] = x_points[route[i]-1]
        y[i] = y_points[route[i]-1]
    plt.scatter(x_points, y_points)
    plt.plot(x, y)
    plt.show()
