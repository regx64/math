import numpy as np
exec(open("slack3.py").read().split("rng=np.random")[0].replace("d=61","d=241"))
print("trQ-/sum(S-1) for regular pair arrays with physical density (spacing s>=2):")
for D in [0.3,1.0,1.5,2.0,3.0]:
    row=[]
    for s in [2.0,2.2,2.5,3.0,4.0,6.0]:
        p=int(d//s); xs=np.arange(p)*(d/p)
        c,n=comb(xs,[D]*p); row.append(f"s={d/p:.2f}:{n:.3f}")
    print(f" Delta={D}: "+"  ".join(row))
