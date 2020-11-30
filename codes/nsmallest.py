def nsmallest(seq, key, n):
  """
  The function is to mimic the heapq.nsmallest() function and to find nth smallest
  items from the list.
  """
  key_fn = lambda x: x[key]
  return(sorted(seq, key = key_fn)[0:n])
