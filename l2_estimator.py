import math


"""
This funtion implements l2 estimator for uniformity testing.
https://theoryofcomputing.org/articles/gs009/gs009.pdf 


Parameters:
n: total number of bins in distribution, {100, 1000, 10000}
epsilon: deviation, a double-float number between [0.1, 0.5]
S: samples taken from the distribution, expected to be a list of numbers
"""
def l2_estimator(n, epsilon, S):
  c_m = 1.76
  c_t = 0.2
  m = math.ceil(c_m*math.sqrt(n)/(epsilon**2) + 1)
  if len(S) < m:
    return "must be at least " +str(m)+" samples"

  coll_k = 0 
  S_dict = {}
  for elt in S:
    if elt in S_dict:
      S_dict[elt] += 1
    else:
      S_dict[elt] = 1


  #Travers the hashtable to count collisions
  for key in S_dict:
    coll = S_dict[key]
    coll_k += coll*(coll - 1)/2

  p = coll_k
  threshold = m*(m-1)/(2*n)+c_t*(m**2)*(epsilon**2)/n
  #compare test statistic with threshold
  if p < threshold:
    return True
  elif p > threshold:
    return False
