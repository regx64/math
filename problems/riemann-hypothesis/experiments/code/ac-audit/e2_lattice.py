import numpy as np
from acmodel import *
print("E2a. Infinite pair lattices: periodic exact model vs fiber formula vs closed form (indicator).")
print("     ratio = tr(Q_-)/sum_k (S(Delta_k)-1).  d=1201 (periodic), M pairs at spacing s=d/M.")
d=1201
for name in ["indicator","taper0.1","MT"]:
    win=Window(name)
    for D in [0.5,1.0]:
        for M in [1201, 800, 601, 480, 400, 300]:
            s=d/M; xs=np.arange(M)*s
            zs,ms=pair_config(xs,[D]*M)
            G=periodic_gram(win,zs,ms,d); 
            imag=np.abs(G.imag).max(); G=G.real
            neg,ev=neg_trace((G+G.T)/2)
            Sd=periodic_S(win,D,d)
            rp=neg/(M*(Sd-1))
            rf=lattice_neg_per_pair(win,s,D)/(win.S(D)-1)
            rc=lattice_ratio_indicator_exact(s,D) if name=="indicator" else float('nan')
            print(f" {name:9s} D={D} s={s:6.3f}: periodic {rp:.5f} | fiber {rf:.5f} | closed {rc:.5f} | trace/zero {np.trace(G)/(2*M):.6f} | max|Im G| {imag:.1e}")
