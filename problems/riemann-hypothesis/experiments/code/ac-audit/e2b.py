import numpy as np
from acmodel import *
print("E2b. min over spacing s in [2,8] (pairs-only local density <= 1) of the lattice ratio; compare bound e^{pi D}/(S-1)")
ss=np.linspace(2,8,1201)
for name in ["indicator","taper0.1","MT","cos2"]:
    win=Window(name)
    for D in [0.25,0.5,1,2,3,5]:
        if name=="indicator":
            r=np.array([lattice_ratio_indicator_exact(s,D) for s in ss])
        else:
            r=np.array([lattice_neg_per_pair(win,s,D,nu0=400)/(win.S(D)-1) for s in ss[::20]]); 
        i=np.argmin(r); sm=(ss if name=="indicator" else ss[::20])[i]
        bound=np.exp(np.pi*D)/(win.S(D)-1)
        r2=lattice_ratio_indicator_exact(2.0,D) if name=="indicator" else lattice_neg_per_pair(win,2.0,D,nu0=2000)/(win.S(D)-1)
        print(f" {name:9s} D={D:4.2f}: ratio(s=2)={r2:.3e}  min_s={r[i]:.3e} at s={sm:.3f}   bound e^(piD)/(S-1)={bound:.3e}")
