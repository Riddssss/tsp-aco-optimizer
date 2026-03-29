import numpy as np
import random

d = np.array([
    [0, 10, 12, 11, 14],
    [10, 0, 13, 15, 8],
    [12, 13, 0, 9, 14],
    [11, 15, 9, 0, 16],
    [14, 8, 14, 16, 0]
])

n = len(d)

def get_eta():
    return 1 / (d + np.eye(n))

def tour_length(tour):
    return sum(d[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def calculate_probabilities(current, unvisited, tau, eta, alpha, beta):
    probs = []
    for j in unvisited:
        probs.append((tau[current][j] ** alpha) * (eta[current][j] ** beta))
    probs = np.array(probs)
    return probs / probs.sum()

def construct_solution(tau, eta, alpha, beta):
    start = random.randint(0, n-1)
    tour = [start]
    unvisited = list(range(n))
    unvisited.remove(start)

    while unvisited:
        current = tour[-1]
        probs = calculate_probabilities(current, unvisited, tau, eta, alpha, beta)
        next_city = np.random.choice(unvisited, p=probs)
        tour.append(next_city)
        unvisited.remove(next_city)

    tour.append(start)
    return tour