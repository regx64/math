# RECOVERED VERBATIM from the transcript of the claude.ai conversation
# "Ground-state rigidity and Riemann Hypothesis" (2026-10-19, chat de654dc8): inline python -c check.
from mpmath import mp,findroot,cosh,sinh,exp,digamma,log,pi,quad,inf
mp.dps=20
f=lambda y: 2*cosh(y/2)-exp(y/2)/(2*sinh(y))
print('y*',findroot(f,0.28))
print('psi(1/4)',digamma(0.25),'c_inf',-log(pi)+digamma(0.25))
print('check',quad(lambda y: exp(-2*y)/y-exp(y/2)/sinh(y),[0,1,inf]))
