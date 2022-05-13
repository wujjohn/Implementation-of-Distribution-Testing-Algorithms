import math
import numpy
import random


"""
Algorithm given by https://cseweb.ucsd.edu//~dakane/testingApproach.pdf
n: number of bins
epsilon: deviation from property
p_u: samples from uniform distribution, over n
q_u: samples from unknown distribution, over n
"""

def lemma_21(n, epsilon, p_u, q_u):
  
  bigOconstant = 5.9
  
  theoretical_SC = int(math.sqrt(n)/(epsilon**2) * bigOconstant)

  p = random.choices(p_u, k=theoretical_SC) 
  q = random.choices(q_u, k=theoretical_SC) 

  Z = 0.0 #test statistic z
  C = 0.45 #constant for threshold

  X = [0.0] * len(p) 
  for i in p:
    X[i] += 1.0
  
  Y = [0.0] * len(q) 
  for i in q:
    Y[i] += 1.0

  for i in range(theoretical_SC):
    if (X[i] + Y[i] != 0): 
      Z = Z + ((X[i] - Y[i])**2 - X[i] - Y[i])/(X[i] + Y[i])

  if (Z <= C * (theoretical_SC**1/2)):
    return True
  else:
    return False
