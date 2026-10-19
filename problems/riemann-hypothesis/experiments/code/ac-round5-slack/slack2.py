import numpy as np
exec(open("slack.py").read().split("d=201")[0])
rng=np.random.default_rng(0)
d=201
def stats(xs,Ds,d):
    Q=np.zeros((d,d))
    for x,D in zip(xs,Ds):
        v=vec(x-1j*D,d); Q+=2*(np.outer(v.real,v.real)-np.outer(v.imag,v.imag))
    ev=np.linalg.eigvalsh(Q)
    trneg=-ev[ev<0].sum(); pos=ev[ev>1e-12]
    slack2=((pos-2)**2).sum()
    ind=np.array([S(D,d)-1 for D in Ds])
    return trneg, ind.sum(), slack2, (ind**2).sum(), np.trace(Q)
print("random configurations (p pairs, Delta ~ U[0,Dmax]):")
for p,Dmax in [(5,1.0),(30,1.0),(30,0.3),(60,0.5),(100,0.2),(100,1.0)]:
    r1=[];r2=[]
    for t in range(5):
        xs=rng.uniform(0,d,p); Ds=rng.uniform(0,Dmax,p)
        a,b,c,e,tr=stats(xs,Ds,d); r1.append(a/b); r2.append(c/e)
    print(f" p={p:3d} Dmax={Dmax}: trQ-/sum(S-1) in [{min(r1):.3f},{max(r1):.3f}]   sum(q-2)^2/sum(S-1)^2 in [{min(r2):.3f},{max(r2):.3f}]")
