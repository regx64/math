import numpy as np
from scipy.optimize import linprog
# For fixed lambda=a1/a0 (a0=1), minimize s=sum_{k>=1} a_k subject to
# a_k>=0 (k>=1), P(theta)=1+sum a_k cos(k theta) >= 0 on a fine grid.
def min_s(lam,K,N=4000):
    th=np.linspace(0,np.pi,N)
    # variables a_2..a_K
    A=-np.cos(np.outer(th,np.arange(2,K+1)))      # -sum a_k cos >= ... 
    b=1+lam*np.cos(th)                              # P>=0  <=>  -sum_{k>=2} a_k cos(k th) <= 1+lam cos th
    c=np.ones(K-1)
    r=linprog(c,A_ub=A,b_ub=b,bounds=[(0,None)]*(K-1),method="highs")
    if r.status!=0: return np.inf,None
    return lam+r.fun, r.x
best=(0,None,None)
for K in [4,8,16,32,48]:
    bK=(0,None)
    for lam in np.linspace(1.01,1.99,197):
        s,_=min_s(lam,K)
        if np.isfinite(s):
            kappa=2*(np.sqrt(lam)-1)**2/s
            if kappa>bK[0]: bK=(kappa,lam,s)
    print(K,"kappa=%.6f at lambda=%.3f, s=%.4f, 1/kappa=%.3f"%(bK[0],bK[1],bK[2],1/bK[0]))
