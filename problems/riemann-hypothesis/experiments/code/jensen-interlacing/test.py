# RECOVERED VERBATIM from the transcript of chat 15786f47 (Jensen interlacing). Requires a.pkl from coeffs.py.
import pickle
from mpmath import mp, mpf, polyroots, factorial, binomial, im, re, nstr
mp.dps = 80
a = [mpf(x) for x in pickle.load(open("a.pkl","rb"))]
c = [factorial(k)*a[k] for k in range(len(a))]   # Jensen (Polya) normalization
def J(g, d, n):  # coefficients low->high
    return [binomial(d,j)*g[n+j] for j in range(d+1)]
def roots(p):    # p low->high
    r = polyroots(list(reversed(p)), maxsteps=400, extraprec=400)
    return r
def real_sorted(r, tol=mpf(10)**-30):
    if any(abs(im(z)) > tol*max(1,abs(z)) for z in r): return None
    return sorted([re(z) for z in r])
def check(g, D, N, label):
    bad_hyp, bad_int, tot = [], [], 0
    for d in range(2, D+1):
        for n in range(0, N+1):
            if n+d >= len(g): continue
            tot += 1
            h = real_sorted(roots(J(g,d,n)))
            A = real_sorted(roots(J(g,d-1,n)))
            Bp = real_sorted(roots(J(g,d-1,n+1)))
            if h is None or len(set(nstr(x,25) for x in h)) < d: bad_hyp.append((d,n))
            ok = A is not None and Bp is not None
            if ok:
                b = Bp + [mpf(0)]
                ok = all(b[j] < A[j] < b[j+1] for j in range(d-1))
            if not ok: bad_int.append((d,n))
            if (h is not None and len(set(nstr(x,25) for x in h))==d) != ok:
                print("LEMMA MISMATCH", label, d, n)
    print(label, "cases:", tot, "non-hyperbolic:", bad_hyp[:10], "interlacing fails:", bad_int[:10])
check(c, 14, 25, "Jensen-normalized gamma(n)=n!*a_n")
check(a, 14, 25, "raw Taylor a_n (user's normalization)")
# Turan / CNV ratio check
for m in range(1, 8):
    print(m, nstr(c[m]**2/(c[m-1]*c[m+1]),12), nstr(a[m]**2/(a[m-1]*a[m+1]),12))
