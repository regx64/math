import numpy as np
from acmodel import *
def Rconst(win, n=4000):
    x,w=leggauss(n); xi=x/2; w=w/2; p2=(WINDOWS[win.name](xi)/win.norm)**2
    return np.sum(w*p2**2) + np.sum((w*p2)[:,None]*(w*p2)[None,:]*np.abs(xi[:,None]-xi[None,:]))
print("E4. Periodic exact model, N = d zeros: L1 off-line pairs at x=0..L1-1 (distance Delta) + (d-2L1) simple on-line")
print("    zeros equally spaced on the rest. Checks the hypotheses Theorem S uses: tr G = N, ||G||_HS^2 <= R N, block structure.")
for name in ["indicator","taper0.1"]:
    win=Window(name); R=Rconst(win)
    print(f" window {name}: R(psi) = {R:.5f}")
    for d in [301,601,1201]:
        for lam1 in [0.08,0.10]:
            L1=int(round(lam1*d)); n2=d-2*L1; s2=(d-L1)/n2
            on=L1-1+s2*(np.arange(n2)+1.0)
            for D in [0.5,1.0]:
                zp,mp=pair_config(np.arange(L1)*1.0,[D]*L1)
                Vp,_=periodic_vectors(win,zp,d); Vo,_=periodic_vectors(win,on.astype(complex),d)
                Qp=(Vp.T@Vp).real; Pon=(Vo.T@Vo).real; G=Qp+Pon
                tr=np.trace(G); hs=np.sum(G*G)
                negQ,_=neg_trace((Qp+Qp.T)/2)
                Sd=periodic_S(win,D,d)
                print(f"  d={d} L1={L1} ({2*L1/d:.3f} of zeros off-line) D={D}: tr/N={tr/d:.6f}  HS/N={hs/d:.4f} (<= R? {hs/d<=R})  "
                      f"tr(Q_-)={negQ:9.3f}  sum(S-1)={L1*(Sd-1):10.2f}  ratio={negQ/(L1*(Sd-1)):.4f}  N0s/N={n2/d:.3f}")
