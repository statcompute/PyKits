def sel_key(seq, key):
  return(list(map(lambda d: {k: d[k] for k in key}, seq)))
