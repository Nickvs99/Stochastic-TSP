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

def plot_scores(scores):

    xs = np.arange(0, len(scores))

    plt.plot(xs, scores)

    plt.title("Distance evolution")
    plt.xlabel("Iteration")
    plt.ylabel("Distance")
    plt.show()

def plot_data(data):

    for a in data:
        
        fig, ax = plt.subplots()

        for b in data[a]:

            score_results = np.array(data[a][b])
            n_iterations = len(score_results[0])

            ys = np.mean(score_results, axis=0)
            ci = np.std(score_results, axis=0)
            xs = range(0, n_iterations)
            
            ax.plot(xs,ys, label=f"b={b}")
            ax.fill_between(xs, ys - ci, ys + ci, alpha=.1)

        ax.set_xlabel("Iterations")
        ax.set_ylabel("Scores")
        plt.title(f"a={a}")
        plt.legend()
        plt.show()

    for b in data[list(data.keys())[0]]:

        fig, ax = plt.subplots()

        for a in data:

            score_results = np.array(data[a][b])
            n_iterations = len(score_results[0])

            ys = np.mean(score_results, axis=0)
            ci = np.std(score_results, axis=0)
            xs = range(0, n_iterations)
            
            ax.plot(xs,ys, label=f"a={a}")
            ax.fill_between(xs, ys - ci, ys + ci, alpha=.1)
        
        ax.set_xlabel("Iterations")
        ax.set_ylabel("Scores")
        plt.title(f"b={b}")
        plt.legend()
        plt.show()