import numpy as np
from scipy.optimize import brentq
a,b=19/24,57/64          # S1 ~ a N L, S2 ~ b N L^2 (Conrey-Ghosh-Gonek, v->1/2)
pmax=(1-0.67250)/2       # off-line pairs per zero allowed by the 2/3 theorem (s1+2p<=N, s1>=0.6725N)
f=lambda eps: max(a-np.sqrt(2*pmax*eps),0)**2/(b+eps)
print("eps=0 ->",f(0),"(=19/27=",19/27,")")
for target in [0.67250,0.68183,0.69,0.70]:
    e=brentq(lambda x:f(x)-target,0,1)
    print(f"to certify {target}: need off-line mollified energy E <= {e:.3e} * N L^2")
