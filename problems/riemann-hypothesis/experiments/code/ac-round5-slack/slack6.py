import numpy as np
exec(open("slack3.py").read().split("rng=np.random")[0].replace("d=61","d=121"))
rng=np.random.default_rng(7)
for D in [1.0,2.0]:
  for s0 in [2.0,3.0]:
    p=int(121//s0); xs=np.arange(p)*(121/p)+rng.normal(0,0.05,p)
    f=lambda x: comb(x,[D]*p)[1]
    cur=f(xs); best=cur
    for it in range(2500):
        y=xs.copy(); i=rng.integers(p); y[i]+=rng.normal(0,0.3)
        # keep physical density: minimum spacing >= 1 (pairs cannot be denser than lattice of zeros)
        ys=np.sort(y%121); gaps=np.diff(np.r_[ys,ys[0]+121])
        if gaps.min()<1.0: continue
        val=f(y)
        if val<cur: xs,cur=y,val
    print(f"Delta={D} start spacing {s0}: local-search minimum of trQ-/sum(S-1) = {cur:.4f} (start {f(np.arange(p)*(121/p)):.4f})")
