import numpy as np
from acmodel import *
"""Sanity check (not a proof) of Theorem A'': finite grid k=0..d-1 (paper's finite matrix, hat units),
one cluster C=[c0,c0+l) of pairs m -+ i*Delta inside the grid.
 Claimed: tr(Q_-) <= tr(G_C)_-  (compression) <= 4*beta + 2*sqrt(l*S*beta),
          beta = sum_{m in C} sum_{k notin C} |v_{m-i Delta}(k)|^2   (sum over ALL integers k not in C)."""
def vrow(win, z, k):
    return v_exact_indicator([z], k)[0] if win.name=="indicator" else I1_vectors2(win, [z], k)[0]
for name in ["indicator","taper0.1"]:
    win=Window(name)
    for D in [0.5,1.0]:
        d=300; c0=100; l=100; grid=np.arange(d); C=np.arange(c0,c0+l)
        zs,ms=pair_config(C*1.0,[D]*l)
        V=np.array([vrow(win,z,grid) for z in zs])
        Q=(V.T@V).real; negQ,_=neg_trace((Q+Q.T)/2)
        # X-block (rows/cols in C)
        X=Q[np.ix_(C,C)]; negX,_=neg_trace((X+X.T)/2)
        # beta: profile |v_{s - i D}| depends only on s=m-k; sum over k notin C (wide range)
        K=200000 if name=="indicator" else 3000
        s=np.arange(-K,K+1); prof=np.abs(vrow(win,-1j*D,-s))**2      # |v_{0-iD}(k)| at k=-s  <=> offset s=m-k
        beta=0.0
        for m in C:
            off=m-np.r_[np.arange(m-K, c0), np.arange(c0+l, m+K+1)]      # s = m - k for k outside C
            beta+=prof[off+K].sum()
        S=win.S(D)
        # bi-infinite cluster negative trace (I2)
        negInf,_=neg_trace(I2_from_A(win,A_pair_segment(l,1.0,D),int(5*(l+1)+300)))
        bound=4*beta+2*np.sqrt(l*S*beta)
        print(f" {name:9s} D={D}: tr(Q_-)={negQ:9.4f}  tr(X_-)={negX:8.4f} (<= 2beta={2*beta:8.4f})  bi-inf tr(G_C)_-={negInf:9.4f}  "
              f"bound 4b+2sqrt(lSb)={bound:9.2f}  l(S-1)={l*(S-1):9.2f}")
