import numpy as np
from acmodel import *
print("E1. Single pair: spectrum vs Lemma B prediction {1+S, 1-S}; trace per zero; I1 (finite grid) vs I2 (bi-infinite)")
for name in ["indicator","taper0.1","MT","cos2"]:
    win=Window(name)
    for D in [0.25,1.0,2.0]:
        zs,ms=pair_config([0.3],[D])
        # I2
        K=I2_matrix(win,zs,ms,n=600); ev=np.linalg.eigvalsh(K); ev=ev[np.abs(ev)>1e-9]
        # I1 on grid of 4001 windows centred on the pair
        k=np.arange(-2000,2001); V=I1_vectors(win,[0.3-1j*D],k)
        sumsq=(V[0]**2).sum(); nrm=(np.abs(V[0])**2).sum()
        S=win.S(D)
        print(f" {name:9s} D={D:4.2f}: S={S:10.4f} | I2 eigs={np.round(np.sort(ev),4)} | pred=({1-S:.4f},{1+S:.4f}) | I1 sum v^2={sumsq.real:.6f}{sumsq.imag:+.1e}i  |v|^2={nrm:.4f}")
