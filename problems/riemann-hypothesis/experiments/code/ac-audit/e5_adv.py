import numpy as np, sys
from acmodel import *
"""Adversarial search, periodic model d=81, pairs only, all at distance Delta.
Admissibility (local counting with excess C): for all i<j (cyclic), gap p_j - p_i >= 2(j-i) - C  [2 zeros per pair].
C=0 forces spacing >= 2 (local density <= 1). Objective: ratio tr(Q_-)/sum(S_d - 1). Simulated annealing with restarts."""
d=81; rng=np.random.default_rng(int(sys.argv[1]) if len(sys.argv)>1 else 0)
def ratio(win,xs,D):
    zs,ms=pair_config(xs,[D]*len(xs)); V,_=periodic_vectors(win,zs,d); G=(V.T@V).real
    neg,_=neg_trace((G+G.T)/2); return neg/(len(xs)*(periodic_S(win,D,d)-1))
def admissible(xs,C):
    p=np.sort(np.mod(xs,d)); n=len(p); P=np.concatenate([p,p+d])
    for i in range(n):
        for k in range(1,n):
            if P[i+k]-P[i] < 2*k - C - 1e-9: return False
    return True
for name in ["indicator","taper0.1"]:
    win=Window(name)
    for D in [1.0,2.0]:
        for C in [0,2]:
            n=30
            base=ratio(win,np.arange(30)*(d/30),D)
            loc2=lattice_ratio_indicator_exact(2.0,D) if win.name=="indicator" else lattice_neg_per_pair(win,2.0,D,nu0=2000)/(win.S(D)-1)
            best=np.inf
            for rs in range(3):
                xs=np.arange(n)*(d/n)+rng.normal(0,0.01,n)
                if not admissible(xs,C): xs=np.arange(n)*(d/n)
                if not admissible(xs,C): continue
                cur=ratio(win,xs,D); T0=0.05*cur
                for it in range(1500):
                    y=xs.copy(); i=rng.integers(n); y[i]+=rng.normal(0,0.4)
                    if not admissible(y,C): continue
                    v=ratio(win,y,D); temp=T0*(1-it/1500)+1e-12
                    if v<cur or rng.random()<np.exp(-(v-cur)/temp): xs,cur=y,v
                    best=min(best,cur)
            print(f" {name:9s} D={D} C={C} n={n}: best found {best:.5f}   (uniform s=2.7 start: {base:.5f}; infinite s=2 lattice: {loc2:.5f})",flush=True)
