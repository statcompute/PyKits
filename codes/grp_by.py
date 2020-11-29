def grp_by(seq, key):
  key_fn = operator.itemgetter(*key)
  lst = sorted(seq, key = key_fn)
  grp = set(map(key_fn, lst))
  return(dict(zip(grp, [[l for l in lst if key_fn(l) == g] for g in grp])))
