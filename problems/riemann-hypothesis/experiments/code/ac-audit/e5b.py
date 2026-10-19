import numpy as np
from acmodel import *
print("E5b. Explicit density-one clusters (pairs at spacing exactly 2, rest of period empty), periodic model.")
for name in ["indicator","taper0.1"]:
    win=Window(name)
    for D in [1.0,2.0]:
        out=[]
        for d,n in [(81,30),(241,100),(601,250),(1201,500)]:
            zs,ms=pair_config(np.arange(n)*2.0,[D]*n); V,_=periodic_vectors(win,zs,d); G=(V.T@V).real
            neg,_=neg_trace((G+G.T)/2); out.append(neg/(n*(periodic_S(win,D,d)-1)))
        inf=lattice_ratio_indicator_exact(2.0,D) if name=="indicator" else lattice_neg_per_pair(win,2.0,D,nu0=2000)/(win.S(D)-1)
        print(f" {name:9s} D={D}: clusters of 30/100/250/500 pairs: "+"  ".join(f"{r:.4f}" for r in out)+f"   -> infinite lattice {inf:.4f}")
