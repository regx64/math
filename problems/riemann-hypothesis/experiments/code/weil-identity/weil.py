import numpy as np, pickle, time
from scipy.special import psi
Z=np.array(pickle.load(open("zeros.pkl","rb")))
def vM(n):
    for p in range(2,n+1):
        if n%p==0:
            m=n
            while m%p==0: m//=p
            return np.log(p) if m==1 else 0.0
    return 0.0
def check(a,omega=0.0,M=3001):
    u=np.linspace(-a,a,M); du=u[1]-u[0]
    x=u/a; f=np.zeros_like(u); ins=np.abs(x)<1
    f[ins]=np.exp(-1/(1-x[ins]**2))
    f=f*np.cos(omega*u)
    def fhat(r):
        r=np.atleast_1d(r); out=np.empty(len(r))
        for i in range(0,len(r),4000):
            out[i:i+4000]=np.cos(np.outer(r[i:i+4000],u))@f*du
        return out
    h=lambda r: fhat(r)**2
    zero_side=2*np.sum(h(Z))
    pole=2*(np.sum(f*np.cosh(u/2))*du)**2
    g0=np.sum(f*f)*du
    g=lambda xx: np.sum(f*np.interp(xx-u,u,f,left=0,right=0))*du
    prime=2*sum(vM(n)/np.sqrt(n)*g(np.log(n)) for n in range(2,int(np.exp(2*a))+1))
    R=np.arange(0,900,0.01)   # h even, psi(1/4+ir/2) real part even
    hR=h(R); w=np.ones_like(R); w[0]=0.5
    arch=-g0*np.log(np.pi)+2*np.sum(w*hR*psi(0.25+0.5j*R).real)*0.01/(2*np.pi)
    rhs=pole+arch-prime
    return zero_side,rhs,pole,arch,prime,g0
for a,om in [(0.3466,0),(1.2,0),(1.6,0),(1.2,30.0)]:
    t=time.time()
    zs,rhs,pole,arch,prime,g0=check(a,om)
    print(f"a={a} omega={om}: zeros={zs:.10f} rhs={rhs:.10f} diff={zs-rhs:.2e} | pole={pole:.6f} arch={arch:.6f} prime={prime:.6f} g0={g0:.6f} ({time.time()-t:.0f}s)",flush=True)
