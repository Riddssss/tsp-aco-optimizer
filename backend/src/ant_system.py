import numpy as np
import time
from src.utils import *

def ant_system(num_ants=10, iterations=50, alpha=1, beta=2, rho=0.5):
    tau = np.ones((n, n))
    eta = get_eta()

    best_tour = None
    best_length = float('inf')

    start_time = time.time()

    for _ in range(iterations):
        all_tours = []

        for _ in range(num_ants):
            tour = construct_solution(tau, eta, alpha, beta)
            length = tour_length(tour)
            all_tours.append((tour, length))

            if length < best_length:
                best_tour = tour
                best_length = length

        tau *= (1 - rho)

        for tour, length in all_tours:
            for i in range(len(tour)-1):
                tau[tour[i]][tour[i+1]] += 1 / length

    return best_tour, best_length, time.time() - start_time