"""
This funtion implements chi-squared tester for identity testing.
https://arxiv.org/pdf/1507.05952.pdf


Parameters:
n: total number of bins in distribution, {100, 1000, 10000}
epsilon: deviation, a double-float number between [0.1, 0.5]
q: weight of the known distribution, expected to be a list of float numbers,
    that length is n and sum of the list is 1
S: samples taken from the distribution, expected to be a list of integers
    that ranges from 0 to (n-1)
"""
def chi_squared(n, epsilon, q, s):
  c_m = 1.45
  c_t = 0.382
  m = int(c_m*(n**0.5)/(epsilon**2))
  if len(S) < m:
    return "must be at least " +str(m)+" samples"
  if n != len(q):
    return "length of q must match n"

  a = [i for i in range(n) if q[i] >= epsilon/(50*n)]

  #generate Ni for i in a
  N = {}
  for i in a:
    N[i] = 0
  for i in s:
    if i not in a:
      continue
    if i not in N:
      N[i] = 1
    else:
      N[i] += 1

  #calculate Z
  Z = sum([((N[i]-m*q[i])**2-N[i])/(m*q[i]) for i in a])

  if Z <= c_t*m*(epsilon**2):
    return True
  else:
    return False
