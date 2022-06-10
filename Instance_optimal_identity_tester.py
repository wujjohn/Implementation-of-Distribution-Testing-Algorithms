""""
http://theory.stanford.edu/~valiant/papers/instanceOpt.pdf

n: number of bins
epsilon: distance to determine is distribution q has the property of distribution p
dist_p: the known distribution with property to be tested against; given the probability of each bin
dist_q: the unknown distribuiton to be tested; given the random variable value of each bin
sroted: if distribution p is given in sorted increasing order
c_1: constant to pin down for sample complexity

**Notice that delta is chosen as 1/3 in the paper**
**For simplicity, generate distribution p in the way that elements of p are in increasing order**
"""

####Simplified version: s=0, does not preprocess p
import math
import random
import statistics
import matplotlib.pyplot as plt 
import numpy as np

def instanceOpt(n, epsilon, dist_p, dist_q, sorted=True):
  if (not sorted):
    dist_p.sort()

  k = 1.8 * max([1/epsilon, two_of_three_norm(dist_p)/(epsilon**2)])
  k = int(np.random.poisson(k))

  s = 0

  samp = random.choices(dist_q, k=k)

  thresh = 0.8*k*(two_of_three_norm(dist_p)**(1/3))
  
  #Count the number of samples in each bin in the samples and store in hashmap
  X = count_samples(samp)

  #Calculate the sums
  sum = 0
  
  for i in range(len(dist_p)):
    if (not (i in X)):
      sum += ((0 - k*dist_p[i])**2 - 0) * ((dist_p[i])**(-2/3))
    else:
      sum += ((X[i] - k*dist_p[i])**2 - X[i]) * ((dist_p[i])**(-2/3))
    
  if (sum>thresh):
    return "Different"
  
  return "Same"

'''
Find the number of times the ith domain element occurs in the samples.

Return the results in a hashset with key represents the ith and value 
represetns the number of counts.
'''
def count_samples(samp):
  S_dict = {}
  for elt in samp:
    if elt in S_dict:
      S_dict[elt] += 1
    else:
      S_dict[elt] = 1

  return S_dict

'''
Find out the 2/3 norm of the given disitribution p
'''
def two_of_three_norm (dist_p):
  two_three_norm = 0
  for p_i in dist_p:
    #print(p_i)
    two_three_norm = two_three_norm + p_i**(2/3)
  
  two_three_norm = two_three_norm**(3/2)

  return two_three_norm
