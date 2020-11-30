def dedup(seq):
  """
  The function de-duplicates the list by values.
  """
  return([dict(t) for t in {tuple(d.items()) for d in seq}])
