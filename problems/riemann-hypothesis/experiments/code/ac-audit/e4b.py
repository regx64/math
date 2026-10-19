import numpy as np
from acmodel import *
exec(open("e4_mixed.py").read().split("print(\"E4.")[0])
print("E4b. Bulk HS/N (extrapolated d->inf from d=601,1201: HS/N = h_bulk + c/d) vs R; taper0.1 and indicator, Delta=0.5")
for name in ["taper0.1","indicator"]:
    win=Window(name); R=Rconst(win)
    for lam1 in [0.10,0.12,0.14,0.16,0.18]:
        vals=[]
        for d in [601,1201]:
            L1=int(round(lam1*d)); n2=d-2*L1; s2=(d-L1)/n2
            on=L1-1+s2*(np.arange(n2)+1.0)
            zp,mp=pair_config(np.arange(L1)*1.0,[0.5]*L1)
            Vp,_=periodic_vectors(win,zp,d); Vo,_=periodic_vectors(win,on.astype(complex),d)
            G=(Vp.T@Vp+Vo.T@Vo).real
            vals.append((d,np.sum(G*G)/d,2*L1/d))
        (d1,h1,f1),(d2,h2,f2)=vals
        hb=(h2*d2-h1*d1)/(d2-d1)   # slope = bulk value
        print(f"  {name:9s} offline fraction {f2:.3f}: bulk HS/N = {hb:.4f}   R = {R:.4f}   admissible(bulk<=R): {hb<=R}")
