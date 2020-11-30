def to_dict(seq):
  """
  The function transposes the list of dicts with same keys to a dict.
  """
  return(dict([(k, [d[k] for d in seq]) for k in seq[0].keys()]))
