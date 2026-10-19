import numpy as np
from scipy.optimize import minimize
exec(open("slack.py").read().split("d=201")[0])
d=61
jj=np.arange(-(d-1)//2,(d-1)//2+1); kk=np.arange(d)
def Qmat(xs,Ds):
    Z=np.array(xs)-1j*np.array(Ds)
    V=np.exp(2j*np.pi*(Z[:,None,None]-kk[None,:,None])*jj[None,None,:]/d).sum(axis=2)/d  # p x d
    return 2*(V.real.T@V.real - V.imag.T@V.imag)
def comb(xs,Ds):
    ev=np.linalg.eigvalsh(Qmat(xs,Ds))
    neg=-ev[ev<0].sum(); pos=ev[ev>1e-12]
    slack=2*neg+((pos-2)**2).sum()
    ind=np.array([S(D,d)-1 for D in Ds])
    return slack/(2*ind.sum()+(ind**2).sum()), neg/ind.sum()
rng=np.random.default_rng(3)
for p,D in [(4,0.3),(8,0.3),(15,0.3),(15,0.6),(25,0.3),(25,0.1)]:
    best=(9,None)
    for trial in range(4):
        x0=rng.uniform(0,d,p)
        f=lambda x: comb(x,[D]*p)[0]
        r=minimize(f,x0,method="Nelder-Mead",options={"maxiter":4000,"xatol":1e-4,"fatol":1e-7})
        if r.fun<best[0]: best=(r.fun,r.x)
    c,n=comb(best[1],[D]*p)
    xs=np.sort(best[1]%d)
    print(f"p={p:2d} Delta={D}: min combined-slack ratio = {c:.4f} (trQ- ratio {n:.4f}); min gap between pair centers = {np.min(np.diff(np.r_[xs,xs[0]+d])):.3f}")
