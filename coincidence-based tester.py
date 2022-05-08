"""
This is an implementation of coincidence-based uniformity tester 
given very sparsely-sampled discrete data.
http://www.stat.columbia.edu/~liam/research/pubs/sparse-unif-test.pdf


Parameters:
n: total number of bins in distribution, {100, 1000, 10000, 100000, 1000000, ...} 
epsilon: deviation (epsilon >> sqrt(2.1)/(n**(1/4)) 
    n = 100: [0.75, 0.9]
    n = 1000: [0.45, 0.9]
    n = 10000: [0.25,0.9]
    n = 100000: [0.15, 0.9]
    n = 1000000: [0.1, 0.9] 
S: samples taken from the distribution, expected to be a list of numbers
    (must be sparsely sampled)
"""

import numpy as np
import math

def coincidence_based_tester(n, epsilon, S):
    # constants for threshold
    c_m = 2.1
    c_t = 0.35 
    
    # number of samples (m << n)
    m = int(c_m*(epsilon**(-2))*(n**(1/2))) 

    if len(S) < m:
        return "must be at least " + str(m) + " samples"
    
    # x is the histogram of samples
    x = []
    x = [0 for i in range(n)]
    
    # x[i] is the number of samples observed to have fallen into the i-th bin
    for elt in S:
      x[elt] += 1

    # non_collisions is the number of bins where just one sample has fallen
    non_collisions = 0

    for i in range(n):
      if x[i] == 1:
        non_collisions += 1

    # non_collisions_uniform is the number of expected non_collisions 
    # when the distribution is uniform
    non_collisions_uniform = m*math.pow((n - 1)/n, m - 1)
    threshold = c_t*((m**2)*(epsilon**2))/n

    Z = non_collisions_uniform - non_collisions

    if Z > threshold:
        return False
    else:
        return True