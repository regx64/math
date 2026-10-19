# RECOVERED VERBATIM from the transcript of chat 15786f47 (Jensen interlacing): first floating-point search.
from mpmath import mp, mpf, polyroots, binomial, im
mp.dps=60
# F(x) = e^{x/4}(x^2+12x+44): gamma_k = F^{(k)}(0)
def g(k):
    p=[44,12,2]
    return sum(binomial(k,j)*mpf(1)/4**(k-j)*p[j] for j in range(min(k,2)+1))
G=[g(k) for k in range(80)]
first=None
for d in range(2,40):
    for n in range(0,40):
        r=polyroots([binomial(d,j)*G[n+j] for j in reversed(range(d+1))],maxsteps=300,extraprec=300)
        if any(abs(im(z))>1e-20 for z in r):
            print("first non-hyperbolic (d,n) with smallest d:",d,n); first=(d,n); break
    if first: break
