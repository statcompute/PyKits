import math 

def cumsum(l):
  return([sum(l[0:(i + 1)]) for i in range(len(l))])

def cumprod(l):
  return([math.prod(l[0:(i + 1)]) for i in range(len(l))])
