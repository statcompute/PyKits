import operator, cytoolz

def inner_join(lseq, rseq, key):
  key_fn = operator.itemgetter(*key)
  return(list(dict(lx, **rx) for lx in lseq for rx in rseq if key_fn(lx) == key_fn(rx)))

def left_join(lseq, rseq, key):
  key_fn = operator.itemgetter(*key)
  return(list(dict(lx, **rx) for lx, rx in
              cytoolz.join(key_fn, lseq, key_fn, rseq, right_default = {})))
