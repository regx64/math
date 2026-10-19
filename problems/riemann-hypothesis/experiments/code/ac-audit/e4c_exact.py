import numpy as np
from scipy.optimize import brentq
from acmodel import *
"""Exact bulk HS density per unit length (normalized int psi^2 = 1):
 - pair lattice spacing 1 (2 zeros/unit): Gram = 2*Toeplitz(psi^2) => HS/unit = 4*int psi^4      (Delta-independent)
 - simple on-line lattice spacing s: HS/unit = (1/s^2) int_{u0 in [-1/2,-1/2+1/s)} (sum_n psi^2(u0+n/s))^2 du0
 Mixed: fraction lam of length with pairs (2 lam N... per unit), rest with on-line spacing s=(1-lam)/(1-2lam): N = d.
 HS/N = 4 lam int psi^4 + (1-lam) h(s).  R(psi) = int psi^4 + iint psi^2 psi^2 |xi-eta|."""
def h_online(win,s,nu=20000):
    u0=-0.5+(np.arange(nu)+0.5)/(nu*s); tot=0
    for a in u0:
        u=a+np.arange(int(np.ceil(s))+2)/s; u=u[u<=0.5]
        tot+=np.sum((WINDOWS[win.name](u)/win.norm)**2)**2
    return tot/(nu*s)/s**2
def Rconst(win,n=3000):
    x,w=leggauss(n); xi=x/2; w=w/2; p2=(WINDOWS[win.name](xi)/win.norm)**2
    return np.sum(w*p2**2)+np.sum((w*p2)[:,None]*(w*p2)[None,:]*np.abs(xi[:,None]-xi[None,:]))
for name in ["indicator","taper0.1","MT"]:
    win=Window(name); R=Rconst(win); I4=np.sum(win.w*win.psi**4)
    H=lambda lam: 4*lam*I4+(1-lam)*h_online(win,(1-lam)/(1-2*lam),nu=4000)
    lam_star=brentq(lambda l:H(l)-R,1e-4,0.3,xtol=1e-6)
    print(f" {name:9s}: R={R:.5f}  int psi^4={I4:.5f}  H(0)={H(1e-9):.5f}  max lam with H<=R: {lam_star:.4f}  => off-line fraction of zeros {2*lam_star:.4f}  (2-R={2-R:.4f})")
