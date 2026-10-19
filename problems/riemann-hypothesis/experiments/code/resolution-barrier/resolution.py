import numpy as np
rng=np.random.default_rng(1)
N=256
# toy periodic configuration on the line: positions in [0,N), marks in {1,2} with total mass N
pos=[];marks=[]
mass=0
while mass<N:
    m=2 if (rng.random()<0.16 and mass+2<=N) else 1
    pos.append(rng.uniform(0,N)); marks.append(m); mass+=m
pos=np.array(pos); marks=np.array(marks)
def points(Delta):
    # each double point -> conjugate pair x +- i*Delta ; simple points stay real
    P=[]
    for x,m in zip(pos,marks):
        if m==1: P.append(complex(x,0))
        else: P+= [complex(x,Delta),complex(x,-Delta)]
    return np.array(P)
def S(Z,alpha):
    A=np.exp(2j*np.pi*alpha*Z).sum()
    B=np.exp(-2j*np.pi*alpha*Z).sum()   # = sum over z' of e^{-2 pi i alpha z'}
    return A*B/N                        # = (1/N) sum_{z,z'} e^{2 pi i alpha (z-z')}
alphas=np.arange(1,N+1)/N
Z0=np.repeat(pos,marks).astype(complex)
S0=np.array([S(Z0,a) for a in alphas])
print("max |Im S0| =",np.abs(S0.imag).max())
D=(marks==2)
for Delta in [1e-1,3e-2,1e-2,3e-3,1e-3]:
    ZD=points(Delta)
    SD=np.array([S(ZD,a) for a in alphas])
    # predicted: A_D = A_0 + (2cosh(2 pi a Delta)-2) * sum_{doubles} e^{2 pi i a x}
    pred=[]
    for a in alphas:
        A0=(marks*np.exp(2j*np.pi*a*pos)).sum()
        dA=(2*np.cosh(2*np.pi*a*Delta)-2)*np.exp(2j*np.pi*a*pos[D]).sum()
        pred.append(abs(A0+dA)**2/N)
    pred=np.array(pred)
    print(f"Delta={Delta:g}: max|Im S_D|={np.abs(SD.imag).max():.1e}  max|S_D-pred|={np.abs(SD.real-pred).max():.1e}  sum_j|s_D-s_0|={np.abs(SD.real-S0.real).sum()/N:.3e}  ratio/Delta^2={np.abs(SD.real-S0.real).sum()/N/Delta**2:.3f}")
p_simple=(marks==1).sum()/N
print("toy law: simple fraction p =",p_simple, " on-line fraction after splitting =",p_simple)
