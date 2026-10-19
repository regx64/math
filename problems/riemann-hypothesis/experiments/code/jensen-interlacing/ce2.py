# RECOVERED VERBATIM from the transcript of chat 15786f47 (Jensen interlacing): exact Sturm count (count_roots).
from sympy import Rational, binomial, Poly, symbols
x=symbols('x')
p=[44,12,2]
def g(k): return sum(binomial(k,j)*Rational(1,4**(k-j))*p[j] for j in range(min(k,2)+1))
G=[g(k) for k in range(120)]
for d in range(2,30):
    fails=[n for n in range(0,60) if Poly(sum(binomial(d,j)*G[n+j]*x**j for j in range(d+1)),x).count_roots()<d]
    if fails: print("d=",d,"non-hyperbolic at n in",fails[:8]); break
