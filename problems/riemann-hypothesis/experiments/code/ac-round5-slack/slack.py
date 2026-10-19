import numpy as np
# periodized indicator window (bandwidth exactly one): Dirichlet kernel D_d(t) = (1/d) sum_{|j|<=(d-1)/2} e^{2 pi i j t/d}
def vec(z,d):
    j=np.arange(-(d-1)//2,(d-1)//2+1)
    k=np.arange(d)
    return (np.exp(2j*np.pi*np.outer(z-k,j)/d).sum(axis=1))/d
def S(Delta,d):
    j=np.arange(-(d-1)//2,(d-1)//2+1)
    return np.mean(np.exp(4*np.pi*j*Delta/d))
d=201
# 1) single pair: eigenvalues of v v^T + vbar vbar^T should be 1+S and -(S-1); trace contribution of each zero = 1
for Delta in [0.0,0.1,0.3,0.5,1.0]:
    v=vec(100.3-1j*Delta,d)
    print("Delta",Delta," sum v^2 =",np.round((v**2).sum(),12)," |v|^2 =",round(np.vdot(v,v).real,6)," S =",round(S(Delta,d),6), end="")
    B=2*(np.outer(v.real,v.real)-np.outer(v.imag,v.imag))
    ev=np.linalg.eigvalsh(B); ev=ev[np.abs(ev)>1e-9]
    print("  block eigenvalues",np.round(ev,6)," predicted",round(1+S(Delta,d),6),round(-(S(Delta,d)-1),6))
