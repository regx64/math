import numpy as np
from scipy.sparse.linalg import eigsh
def vM_table(N):
    L=np.zeros(N+1)
    sieve=np.ones(N+1,bool); sieve[:2]=False
    for p in range(2,N+1):
        if sieve[p]:
            sieve[p*p::p]=False
            q=p
            while q<=N: L[q]=np.log(p); q*=p
    return L
N=10**6; Lam=vM_table(N)
c=np.zeros(N+1); n=np.arange(N+1); c[2:]=Lam[2:]/np.sqrt(n[2:])
S=np.cumsum(c)
t0=3e12
target=0.5*np.log(t0/(2*np.pi))
print("target 1/2 log(t0/2pi) at t0=3e12:", target)
X=np.argmax(S>target); print("rigorous trivial bound: need S(X)>target -> X >=",X," S(X-1)=",S[X-1]," a>=",0.5*np.log(X))
# lambda_max(a): top eigenvalue of Q(phi)=sum_n c_n int phi(v)phi(v-log n)dv on L^2[-a,a]
def lam_max(a,M=1500):
    h=2*a/(M-1)
    A=np.zeros((M,M))
    for m in range(2,int(np.exp(2*a))+1):
        if c[m]==0: continue
        Lsh=np.log(m)/h; k=int(np.floor(Lsh)); th=Lsh-k
        for kk,w in ((k,1-th),(k+1,th)):
            if kk<M:
                idx=np.arange(kk,M)
                A[idx,idx-kk]+=c[m]*w*h
    A=(A+A.T)/2  # symmetric part (form is symmetric in exact arithmetic)
    # form value phi^T A phi / (h*|phi|^2)
    ev=np.linalg.eigvalsh(A/h)
    return ev[-1]
for a in [0.3466,1.0,1.5,2.0,2.5,3.0,3.5,4.0]:
    print(f"a={a}: lambda_max={lam_max(a):.4f}  trivial S(e^2a)={S[int(np.exp(2*a))]:.4f}")
