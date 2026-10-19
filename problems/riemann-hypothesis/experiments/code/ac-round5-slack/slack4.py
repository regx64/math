import numpy as np
exec(open("slack3.py").read().split("rng=np.random")[0].replace("d=61","d=241"))
print("regular arrays of pairs (spacing s, all same Delta) filling the period; retained-slack ratios")
for D in [0.05,0.1,0.3,0.6,1.0]:
    row=[]
    for s in [0.5,0.7,0.8,0.9,1.0,1.2,1.5,2.0,3.0]:
        p=int(d//s); xs=np.arange(p)*(d/p)
        c,n=comb(xs,[D]*p); row.append(f"s={d/p:.2f}:{c:.3f}/{n:.3f}")
    print(f"Delta={D}: "+"  ".join(row))
