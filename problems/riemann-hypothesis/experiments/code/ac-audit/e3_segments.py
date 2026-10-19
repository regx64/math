import numpy as np, sys
from acmodel import *
print("E3. Finite segment of L pairs, spacing s, distance Delta; bi-infinite grid (I2 via closed-form A). ratio = tr(Q_-)/(L(S-1))")
Ls=[1,2,4,8,16,32,64,128,256,512]
for name in ["indicator","taper0.1"]:
    win=Window(name)
    for s in [1.0,1.5,2.0]:
        for D in [0.5,1.0,2.0]:
            row=[]
            for L in Ls:
                n=int(5*(L*s+1)+300)
                neg,_=neg_trace(I2_from_A(win,A_pair_segment(L,s,D),n))
                row.append(neg/(L*(win.S(D)-1)))
            n=int(5*(512*s+1)+300); neg2,_=neg_trace(I2_from_A(win,A_pair_segment(512,s,D),int(1.5*n)))
            print(f" {name:9s} s={s} D={D}: "+" ".join(f"{r:.4f}" for r in row)+f"  [n x1.5 diff {abs(neg2/(512*(win.S(D)-1))-row[-1]):.1e}]",flush=True)
