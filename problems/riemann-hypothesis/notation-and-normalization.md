# Notation and normalization

Several normalizations were used during the project. Each note says which one it uses. This file is the canonical reference; when a note and this file disagree, this file wins and the note should be corrected.

## 0. Scope tags (used everywhere in the archive)

Every claim carries one of these tags. A result proved under one tag is **never** promoted to a stronger tag.

| Tag | Meaning |
|---|---|
| **[M]** | Statement about finite (or bi-infinite) matrices built from an *arbitrary* finite family of points; no arithmetic input. |
| **[D]** | Statement about abstract zero configurations satisfying *selected* numerical constraints, e.g. trace and Hilbert–Schmidt values or the Riemann–von Mangoldt count. |
| **[PI]** | Statement under the full analytic hypotheses `PaperInputs` of the Alpöge–Furman formalization (explicit formula H-EF, Riemann–von Mangoldt H-RvM, Chebyshev–Mertens, Montgomery–Vaughan, Γ-facts). See [formalization/README.md](formalization/README.md). |
| **[ζ]** | Statement about the actual nontrivial zeros of the Riemann zeta function. |

## 1. Zeros

- Nontrivial zero: $\rho=\beta+it$, with $0<\beta<1$. Trivial zeros are $-2,-4,\dots$; the pole is at $s=1$.
- Complex ordinate (Lean `gammaOf`): $\gamma_\rho=(\rho-\tfrac12)/i$. For $\rho=\tfrac12+\delta+it$ this gives $\gamma_\rho=t-i\delta$. A zero is off the critical line iff $\operatorname{Im}\gamma_\rho\neq0$.
- Reflection (Lean `reflect`): $\rho\mapsto1-\bar\rho$. It sends $\gamma\mapsto\bar\gamma$ and preserves multiplicity (`mult_reflect`).
- Off-line quadruple: $\{\rho,\bar\rho,1-\rho,1-\bar\rho\}$.

## 2. Fourier conventions (four different ones were used)

| Where | Convention |
|---|---|
| Alpöge–Furman paper and Lean (`paperFT`, `Defs.lean:44`) | $\hat f(z)=\int f(u)e^{izu}\,du$ |
| Smoothed explicit formula, approaches/02 | Laplace form $G(z)=\int g(u)e^{zu}\,du$ |
| Guinand–Weil form, approaches/03 | $h(r)=\int g(u)e^{iru}\,du$ with $g=f*f^*$, $f^*(u)=f(-u)$ |
| AC work in normalized frequency, AC/ | $v_\zeta(k)=\int_{-1/2}^{1/2}\psi(\xi)\,e^{2\pi i\xi(\zeta-k)}\,d\xi$ |

## 3. Grid, window and units of the 2/3 paper (canonical for AC/)

From `Zeta23/Defs.lean`:
- $L=\lambda\log(T/2\pi)$ with $0<\lambda\le1$; the 2/3 theorem uses $\lambda=1$.
- Grid step $h=2\pi/L$, grid size $d=\lfloor LT/2\pi\rfloor$, grid points $\tau_k=T+kh$.
- Window $\varphi(u)=\varrho\bigl((L/2-|u|)/w\bigr)$, where $\varrho\in C^3$ is a taper ($0$ on $(-\infty,0]$, $1$ on $[1,\infty)$) and $w\ge1$.
- $a=L^{-1}\int\varphi^2$, with $a\ge\tfrac12$ (Lean `half_le_a`).
- Evaluation vector $u_\rho(k)=\hat\varphi(\gamma_\rho-\tau_k)$ for $0\le k<d$.
- Units: hat units $\hat M=M/(aL^2)$ and tilde units $\tilde M=M/L$.

Normalized form (derived in [AC/03-E6-audit.md](AC/03-E6-audit.md) §B):
$$
\hat u_\rho(k)=\frac{u_\rho(k)}{L\sqrt a}=\int_{-1/2}^{1/2}\psi_L(\xi)\,e^{2\pi i\xi(\zeta_\rho-k)}\,d\xi,\qquad
\psi_L(\xi)=\frac{\varphi(L\xi)}{\sqrt a},\quad \int\psi_L^2=1,\quad \zeta_\rho=\frac{(\gamma_\rho-T)L}{2\pi}.
$$
- For an off-line zero, $\zeta=x-i\Delta$ with **normalized distance** $\Delta=\delta L/2\pi$, where $\delta=\beta-\tfrac12$.
- Δ is measured in grid units. It equals zero-spacing units only when $\lambda=1$.
- **Δ enters the evaluation vector itself**, through the factor $e^{2\pi\xi\Delta}$.
- $\psi_L$ depends on $L$ and tends to the indicator of $[-\tfrac12,\tfrac12]$ as $L/w\to\infty$.

## 4. Gram matrices and blocks

- $\hat A=\sum_{\rho\in Z(I')}m_\rho\,\hat u_\rho\hat u_\rho^{\mathsf T}$. This is a **transpose**, not an adjoint (Lean `blockA`, `ZeroSide.lean:316`). It is real symmetric because the zero set is reflection-invariant.
- $I'=(T-\sqrt T,\,2T+\sqrt T]$ (`Defs.lean:67`). The window is wider than the grid range.
- Paper's blocks: $P$ = all on-line zeros, simple and multiple (`blockP`); $Q$ = off-line pairs only (`blockQ`). So the paper's $Q$ is $Q^{\mathrm{pairs}}$.
- AC notes: $P_1$ = simple on-line zeros only; $Q'=\hat A-P_1=M+Q^{\mathrm{pairs}}$, where $M$ is the multiple on-line part.
- Pair block: $m(uu^{\mathsf T}+\bar u\bar u^{\mathsf T})=2m(xx^{\mathsf T}-yy^{\mathsf T})$ with $u=x+iy$ (Lean `pair_term`).
- $\operatorname{tr}(X)_-$ is the sum of the absolute values of the negative eigenvalues of a Hermitian $X$. It is subadditive, and $\operatorname{tr}(A-B)_-\le\|B\|_1$ when $A\succeq0$.
- $S_\psi(\Delta)=\int\psi(\xi)^2\cosh(4\pi\Delta\xi)\,d\xi$ with $\int\psi^2=1$. For the indicator, $S(\Delta)=\sinh(2\pi\Delta)/(2\pi\Delta)$.
- $R(\psi)=\int\psi^4+\iint\psi^2(\xi)\psi^2(\eta)\,|\xi-\eta|\,d\xi\,d\eta$, with value $4/3$ for the indicator.

  **Provisional identification:** the paper's $R(\psi)$ formula uses its own window, which we take to be our $\psi^2$. This matches at the indicator ($4/3$) and has not been checked against the paper text.

## 5. Normalized ordinates for pair-correlation certificates (approaches/04, 05)

- $z=\gamma\log T/2\pi$, so that mean spacing is 1.
- Form factor of a reflection-invariant configuration: $S(\alpha)=|A(\alpha)|^2/N$ with $A(\alpha)=\sum_ze^{2\pi i\alpha z}$. Here $B=\bar A$ because of reflection invariance.
- Grid masses: $s_j=S(j/N)/N$ (Lean `PairCeiling/Defs.lean`, `Bridge.lean` `massOf`).

## 6. Guinand–Weil form (approaches/03)

For real $f\in C^2_c([-a,a])$, $g=f*f^*$ and $h(r)=\hat f(r)\overline{\hat f(\bar r)}$:
$$
W(g):=\sum_\rho h(\gamma_\rho)=\underbrace{h(\tfrac i2)+h(-\tfrac i2)}_{\text{Pole}}\;\underbrace{-\,g(0)\log\pi+\frac1{2\pi}\int h(r)\operatorname{Re}\psi\bigl(\tfrac14+\tfrac{ir}2\bigr)dr}_{A(g)}\;-\;\underbrace{2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,g(\log n)}_{P(g)} .
$$
Weil's criterion: RH $\iff W\ge0$ for all such $f$ with Pole $=0$.
