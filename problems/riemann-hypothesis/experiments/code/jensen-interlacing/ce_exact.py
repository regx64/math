# RECOVERED from the transcript of chat 15786f47 (three inline sympy checks merged into one file;
# the code lines are verbatim, only the print labels were added). Counterexample kernel
# K(u)=e^{-u^2}(1+u^4/2): F(x)=e^{x/4}(x^2+12x+44), gamma_k = F^{(k)}(0).
from sympy import Rational, binomial, Poly, symbols, nroots, real_roots
x=symbols('x'); p=[44,12,2]
g=lambda k: sum(binomial(k,j)*Rational(1,4**(k-j))*p[j] for j in range(min(k,2)+1))
print("[d=4 check] J_{4,0} and its roots")
P=sum(binomial(4,j)*g(j)*x**j for j in range(5)); print(P); print(nroots(P,n=15))
print([g(k) for k in range(5)])
print("[real-root count with multiplicity] d, list of n<40 where J_{d,n} is NOT hyperbolic")
G=[g(k) for k in range(80)]
for d in range(2,12):
    f=[n for n in range(0,40) if len(real_roots(Poly(sum(binomial(d,j)*G[n+j]*x**j for j in range(d+1)),x)))<d]
    print(d, f[:12], '...' if len(f)>12 else '')
