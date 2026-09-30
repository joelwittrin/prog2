""" MA3.py

Student:
Mail:
Reviewed by:
Date reviewed:

File path for MA3 may need to be copied into test files in order to execute +
Save png files for Exc1 before turning in!
"""

import random
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc
from numba import njit


# Exc1
def approximate_pi(n):

    nc_x = []
    nc_y = []
    ns_x = []
    ns_y = []

    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if m.sqrt(x**2 + y**2) <= 1:
            nc_x.append(x)
            nc_y.append(y)
        else:
            ns_x.append(x)
            ns_y.append(y)

    n_total = len(nc_x) + len(ns_x)
    pi = 4 * len(nc_x) / n_total

    plt.scatter(nc_x, nc_y, color = 'r')
    plt.scatter(ns_x, ns_y, color = 'b')
    plt.show()
    plt.title(f'{n} points with pi ≈ {pi}')

    print(f'Estimated pi for {n} dots: {pi}')
    return pi


# Exc2, approximation
def sphere_volume(n, d): 

    r = 1
    n_in = 0
    n_out = 0

    for _ in range(n):
        x_vals = [random.uniform(-1,1) for x in range(d)]

        norm = sum ( map(lambda x: x**2, x_vals) )

        if norm <= 1:
            n_in += 1
        else:
            n_out += 1

    # n_in / n = V_sphere / V_dimension
    n_total = n_in + n_out
    V_sphere = (n_in / n_total) * 2**d

    return V_sphere

#Exc2, real value
def hypersphere_exact(n, d):
    r = 1
    return ( m.pi**(d/2) / (m.gamma(d/2 + 1)) ) * r**d


#Exc3: numba version
@njit
def sphere_volume_numba(n:int, d:int)->float:

    r = 1
    n_in = 0
    n_out = 0

    for _ in range(n):
        x_vals = [random.uniform(-1,1) for x in range(d)]

        norm = sum([x**2 for x in x_vals])

        if norm <= 1:
            n_in += 1
        else:
            n_out += 1

    # n_in / n = V_sphere / V_dimension
    n_total = n_in + n_out
    V_sphere = (n_in / n_total) * 2**d

    return V_sphere


#Exc4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel(n, d, np=10):

    n_per_process = n // np
    with future.ProcessPoolExecutor() as ex:

        processes_lst = []
        for _ in range(np):
            process = ex.submit(sphere_volume, n_per_process, d)
            processes_lst.append(process)

        results = []
        for p in processes_lst:
            volume = p.result()
            results.append(volume)


    return sum(results) / len(results)


def main():
    # Exc1
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)
        
    print('\n')


    # Exc2
    n = 100000
    d = 2
    sphere_volume(n, d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")
    print(f'Approx. volume of {d} dimentional sphere = ', sphere_volume(n, d))

    n = 100000
    d = 11
    sphere_volume(n, d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")
    print(f'Approx. volume of {d} dimentional sphere = ', sphere_volume(n, d))

    print('\n')


    # Exc3
    for _ in range(3):
        n = 1000000
        d = 11

        start = pc()
        sphere_volume(n, d)
        stop = pc()
        print(f"Exc3: Sequential time of {d} and {n}: {stop-start}")

    for _ in range(3):
        start = pc()
        sphere_volume_numba(n, d)
        stop = pc()
        print(f"Exc3: Sequential time of {d} and {n} for numba: {stop-start}")

    print('\n')


    # Exc4
    n = 1000000
    d = 11

    start = pc()
    sphere_volume(n, d)
    stop = pc()
    print(f"Exc4: Sequential time of {d} and {n}: {stop-start}")

    start = pc()
    sphere_volume_parallel(n, d)
    stop = pc()
    print(f"Exc4: Parallell time: {stop-start}")


if __name__ == '__main__':
	main()

'''
ssh jowi.6917@gullviva.it.uu.se
'''

