"""
AC audit harness.  Normalized units: window centers at integers k (grid step h = 2*pi/L -> 1),
window psi supported in [-1/2,1/2] (frequency variable xi), normalized int psi^2 = 1.
Evaluation vector of a zero at normalized complex ordinate z:
    v_z(k) = int psi(xi) exp(2 pi i xi (z - k)) dxi           (paper: phi_hat(gamma - tau_k), rescaled)
Gram matrix (paper G~):  G = sum_rho m_rho v_rho v_rho^T   (TRANSPOSE, not adjoint); real symmetric
when the zero multiset is invariant under z -> conj(z)  (rho -> 1 - conj(rho)).
Off-line pair at normalized distance Delta: z = x -+ i*Delta.

Implementation I1 (position domain): finite grid k = k0..k1, vectors by quadrature, explicit sum.
Implementation I2 (frequency domain, bi-infinite grid): G is unitarily equivalent to the operator
    K(eta, xi) = psi(eta) psi(xi) A(xi - eta),   A(beta) = sum_rho m_rho exp(2 pi i beta z_rho)
on L^2[-1/2,1/2]; discretized with Gauss-Legendre nodes.
Implementation I3: closed form / fiber formula for infinite lattices.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss

# ---------------- windows (unnormalized shapes on [-1/2,1/2]) ----------------
def taper_profile(t):            # C^3-ish smooth step 0->1 on [0,1]
    t = np.clip(t, 0, 1)
    return t**4 * (35 - 84*t + 70*t**2 - 20*t**3)
WINDOWS = {
    "indicator": lambda u: np.ones_like(u),
    "taper0.1":  lambda u: taper_profile((0.5 - np.abs(u)) / 0.1),
    "taper0.3":  lambda u: taper_profile((0.5 - np.abs(u)) / 0.3),
    "MT":        lambda u: np.cos(np.sqrt(2) * u),
    "cos2":      lambda u: np.cos(np.pi * u)**2,
}

class Window:
    def __init__(self, name, nq=400):
        self.name = name
        x, w = leggauss(nq)
        self.xi = x / 2; self.w = w / 2
        f = WINDOWS[name](self.xi)
        self.norm = np.sqrt(np.sum(self.w * f**2))
        self.psi = f / self.norm                      # int psi^2 = 1
    def S(self, Delta):                               # S_psi(Delta) = int psi^2 cosh(4 pi Delta xi)
        return np.sum(self.w * self.psi**2 * np.cosh(4*np.pi*Delta*self.xi))

# ---------------- I2: frequency-domain Toeplitz operator ----------------
def I2_matrix(win, zs, ms, n=None):
    zs = np.asarray(zs, complex); ms = np.asarray(ms, float)
    ext = np.ptp(zs.real) + 1 if len(zs) else 1
    if n is None: n = int(min(4000, 6*ext + 300))
    x, w = leggauss(n); xi = x/2; w = w/2
    psi = WINDOWS[win.name](xi) / win.norm
    B = xi[None, :] - xi[:, None]                     # beta = xi_j - xi_i
    A = np.zeros_like(B, dtype=complex)
    for z, m in zip(zs, ms):
        A += m * np.exp(2j*np.pi*B*z)
    sw = np.sqrt(w)
    K = (sw*psi)[:, None] * A * (sw*psi)[None, :]
    K = (K + K.conj().T) / 2
    return K

# ---------------- I1: position-domain finite grid ----------------
def I1_vectors(win, zs, k):
    D = np.asarray(zs, complex)[:, None] - np.asarray(k, float)[None, :]      # (#z, #k)
    E = np.exp(2j*np.pi*D[:, :, None]*win.xi[None, None, :])               # (#z, #k, nq)
    return E @ (win.w * win.psi)                                            # (#z, #k)
def I1_matrix(win, zs, ms, k):
    V = I1_vectors(win, zs, k)
    G = (V.T * np.asarray(ms, float)) @ V                            # sum m v v^T
    return G

# ---------------- spectral functionals ----------------
def neg_trace(M):
    ev = np.linalg.eigvalsh(M)
    return -ev[ev < 0].sum(), ev

def pair_config(xs, Ds):
    zs, ms = [], []
    for x, D in zip(xs, Ds):
        zs += [x - 1j*D, x + 1j*D]; ms += [1, 1]
    return zs, ms

# ---------------- I3: infinite lattice of pairs, spacing s, distance Delta ----------------
def lattice_neg_per_pair(win, s, Delta, nu0=4000):
    """tr(Q_-)/#pairs for the infinite lattice {m s -+ i Delta}: fiber formula
       int_{u0 in [-1/2,-1/2+1/s)} [ sqrt(E_+ E_-) - E_0 ] du0,
       E_sig(u0) = sum_{n>=0, u0+n/s<=1/2} psi(u0+n/s)^2 exp(4 pi sig Delta (u0+n/s))."""
    u0 = -0.5 + (np.arange(nu0) + 0.5) / (nu0 * s)
    tot = 0.0
    for a in u0:
        u = a + np.arange(int(np.ceil(s)) + 2) / s
        u = u[u <= 0.5]
        p2 = (WINDOWS[win.name](u) / win.norm)**2
        Ep = np.sum(p2*np.exp(4*np.pi*Delta*u)); Em = np.sum(p2*np.exp(-4*np.pi*Delta*u)); E0 = np.sum(p2)
        tot += np.sqrt(Ep*Em) - E0
    return tot / (nu0 * s)

def lattice_ratio_indicator_exact(s, Delta):
    """closed form, indicator window, continuum: classes of size floor(s), ceil(s), a = 2 pi Delta / s."""
    a = 2*np.pi*Delta/s
    k0 = int(np.floor(s)); f = s - k0
    g = lambda k: (np.sinh(k*a)/np.sinh(a) - k) if k >= 1 else 0.0
    neg = ((1-f)*g(k0) + f*g(k0+1)) / s
    S = np.sinh(2*np.pi*Delta)/(2*np.pi*Delta)
    return neg / (S - 1)

# ---- corrected I1: exact sinc for the indicator; adaptive quadrature otherwise ----
def v_exact_indicator(zs, k):
    t = np.asarray(zs, complex)[:, None] - np.asarray(k, float)[None, :]
    out = np.ones_like(t)
    nz = np.abs(t) > 1e-14
    out[nz] = np.sin(np.pi*t[nz]) / (np.pi*t[nz])
    return out
def I1_vectors2(win, zs, k):
    if win.name == "indicator":
        return v_exact_indicator(zs, k)
    span = np.max(np.abs(np.asarray(zs, complex).real[:, None] - np.asarray(k)[None, :])) + 1
    nq = int(6*span + 200)
    x, w = leggauss(nq); xi = x/2; w = w/2
    psi = WINDOWS[win.name](xi) / win.norm
    out = np.empty((len(zs), len(k)), complex)
    for i, z in enumerate(zs):
        E = np.exp(2j*np.pi*np.subtract.outer(z, np.asarray(k, float))[:, None]*xi[None, :])
        out[i] = E @ (w*psi)
    return out
def I1_matrix2(win, zs, ms, k):
    V = I1_vectors2(win, zs, k)
    return (V.T * np.asarray(ms, float)) @ V

# ---- periodic model (exact, no edges): d windows, frequencies j/d, |j| <= (d-1)/2, d odd ----
def periodic_vectors(win, zs, d):
    j = np.arange(-(d-1)//2, (d-1)//2 + 1)
    pj = WINDOWS[win.name](j/d); pj = pj / np.sqrt(np.mean(pj**2))     # (1/d) sum psi_j^2 = 1
    k = np.arange(d)
    Z = np.asarray(zs, complex)
    C = np.exp(2j*np.pi*np.outer(Z, j)/d) * pj[None, :]                 # (#z, d)
    F = np.exp(-2j*np.pi*np.outer(j, k)/d) / d                          # (d, d)
    return C @ F, pj
def periodic_S(win, Delta, d):
    j = np.arange(-(d-1)//2, (d-1)//2 + 1)
    pj = WINDOWS[win.name](j/d); pj = pj / np.sqrt(np.mean(pj**2))
    return np.mean(pj**2 * np.cosh(4*np.pi*Delta*j/d))
def periodic_gram(win, zs, ms, d):
    V, _ = periodic_vectors(win, zs, d)
    return (V.T * np.asarray(ms, float)) @ V

def I2_from_A(win, Afun, n):
    x, w = leggauss(n); xi = x/2; w = w/2
    psi = WINDOWS[win.name](xi) / win.norm
    B = xi[None, :] - xi[:, None]
    sw = np.sqrt(w)
    K = (sw*psi)[:, None] * Afun(B) * (sw*psi)[None, :]
    return (K + K.conj().T) / 2
def A_pair_segment(L, s, D, x0=0.0):
    # sum_{m<L} 2 cosh(2 pi beta D) e^{2 pi i beta (x0 + m s)}
    def A(B):
        num = np.exp(2j*np.pi*B*s*L) - 1; den = np.exp(2j*np.pi*B*s) - 1
        small = np.abs(den) < 1e-12
        Dk = np.where(small, L, num/np.where(small, 1, den))
        return 2*np.cosh(2*np.pi*B*D) * np.exp(2j*np.pi*B*x0) * Dk
    return A
