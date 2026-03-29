import numpy as np
import time
from src.utils import *

def max_min_as(num_ants=10, iterations=50, alpha=1, beta=2, rho=0.5):
    tau = np.ones((n, n))
    eta = get_eta()

    best_tour = None
    best_length = float('inf')

    tau_max = 10
    tau_min = 0.1

    start_time = time.time()

    for _ in range(iterations):
        for _ in range(num_ants):
            tour = construct_solution(tau, eta, alpha, beta)
            length = tour_length(tour)

            if length < best_length:
                best_tour = tour
                best_length = length

        tau *= (1 - rho)

        for i in range(len(best_tour)-1):
            tau[best_tour[i]][best_tour[i+1]] += 1 / best_length

        tau = np.clip(tau, tau_min, tau_max)

    return best_tour, best_length, time.time() - start_time