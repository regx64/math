import numpy as np, pickle, mpmath
mpmath.mp.dps=30
# 1) N(t) <= (t/2pi) log t for t>=10 using Trudgian (2014) upper bound
t=np.logspace(1,16,200001)
trud=t/(2*np.pi)*np.log(t/(2*np.pi))-t/(2*np.pi)+7/8+0.112*np.log(t)+0.278*np.log(np.log(t))+2.510+1/(5*t)
print("min margin (t/2pi)log t - Trudgian upper:", np.min(t/(2*np.pi)*np.log(t)-trud))
Z=np.array(pickle.load(open("zeros.pkl","rb")))
tt=np.linspace(10,700,5000); Nt=np.searchsorted(Z,tt)
print("actual zeros check, min of (t/2pi)log t - N(t):", np.min(tt/(2*np.pi)*np.log(tt)-Nt))
# 2) exact S(66), S(67) with high precision
def Lam(n):
    for p in range(2,n+1):
        if n%p==0:
            m=n
            while m%p==0: m//=p
            return mpmath.log(p) if m==1 else 0
S=lambda X: mpmath.fsum(Lam(n)/mpmath.sqrt(n) for n in range(2,X+1))
target=mpmath.log(mpmath.mpf(3)*10**12/(2*mpmath.pi))/2
print("target=",target," S(66)=",S(66)," S(67)=",S(67), " half-log(67)=",mpmath.log(67)/2)
# 3) tail constant at T0=3e12
T0=3e12
print("2(log T0+1)/(pi T0) =", 2*(np.log(T0)+1)/(np.pi*T0), "  times 2 (||g''||<=2a||f'||^2):", 4*(np.log(T0)+1)/(np.pi*T0))
# 4) psi(1/4) - log pi
print("psi(1/4)-log(pi)=", mpmath.digamma(0.25)-mpmath.log(mpmath.pi), " psi(3/2)=",mpmath.digamma(1.5))
