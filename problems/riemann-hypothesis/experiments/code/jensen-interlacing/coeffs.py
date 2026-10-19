# RECOVERED VERBATIM from the transcript of the claude.ai conversation
# "Jensen polynomial interlacing for Riemann hypothesis" (2026-10-19, chat 15786f47).
# Originally run in /tmp/rh of another session; output not preserved there.
from mpmath import mp, mpf, quad, exp, pi, factorial, inf, zeta, gamma
mp.dps = 80
def Phi(u):
    s = mpf(0)
    for n in range(1, 12):
        s += (2*pi**2*n**4*exp(9*u/2) - 3*pi*n**2*exp(5*u/2))*exp(-pi*n**2*exp(2*u))
    return s
M = 45
a = []
for m in range(M):
    I = quad(lambda u: u**(2*m)*Phi(u), [0, 0.5, 1, 1.5, 2, 3, 4, 6])
    a.append(2*I/factorial(2*m))
xi_half = mpf(0.5)*mpf(0.5)*(-mpf(0.5))*pi**(-mpf(0.25))*gamma(mpf(0.25))*zeta(mpf(0.5))
print("a0 =", mp.nstr(a[0], 20), " xi(1/2) =", mp.nstr(xi_half, 20))
import pickle; pickle.dump([str(x) for x in a], open("a.pkl","wb"))
for m in range(6): print(m, mp.nstr(a[m], 15))
