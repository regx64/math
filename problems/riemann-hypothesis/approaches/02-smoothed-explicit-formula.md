# 02 — Positivity of Λ with a smoothed explicit formula (Landau / de la Vallée Poussin route)

**Phases** P1 (2026-10-18 23:57) and P2 (2026-10-19 00:03–00:24), main conversation. **Scope [ζ]**, with [M]-type method limits.

**Normalization.** Laplace form $G(z)=\int g(u)e^{zu}du$ with $g\ge0$, plus a nonnegative cosine polynomial $P(\theta)=a_0+\sum_ka_k\cos k\theta$.

## Idea

Evaluate
$$\sum_n\Lambda(n)n^{-\sigma}g(\log n)P(t\log n)\ \ge\ 0$$
at the hypothetical zero, using an exact explicit formula valid inside the strip. The aim was to make the $\rho_0$ term outweigh the pole term.

## Lemmas (as audited in P2)

| ID | Statement | Status |
|---|---|---|
| EF-L1 | For $g\in C^2$ with support in $[u_1,u_2]$ and $u_1>0$: $\sum\Lambda(n)n^{-s}g(\log n)=G(1-s)-\sum_\rho m_\rho G(\rho-s)-\sum_mG(-2m-s)$, all sums absolutely convergent. **Fails for non-compact $g$**: the trivial-zero sum diverges and the archimedean term $\tfrac12\psi$ appears instead. | PROVED (standard contour argument; uses Davenport Ch. 17 bounds) |
| EF-L2 | The positivity inequality obtained from L1 and $P\ge0$ | PROVED |
| EF-L3 | Pole dominance: if $\bar u(1-\beta_0)\ge\log4$, then $a_1[G(0)+G(1-2\beta_0)]<a_0G(1-\beta_0)$. Uses Fejér–Egerváry $\lvert a_1\rvert<2a_0$ and Jensen. Using it for a contradiction also needs $a_1>0$ and $a_k\ge0$. | PROVED |
| EF-L4 | Zero-sum bound and the claimed "de la Vallée Poussin width" deduction | **REFUTED/WITHDRAWN.** It counted zeros in windows of width $Y<1$ as $\ll Y\log T$, which is not known. With compact kernels the ratio is $\log T$ at every width. |
| EF-L5 | Reflection invariance: at $\sigma=1-\beta_0$ the pole-to-zero weight ratio is $e^{u(1-\beta_0)}$ again | PROVED |
| EF-L6 | Landau: $\psi(x)-x=O(x^a)$ implies $\zeta\ne0$ for $\operatorname{Re}s>a$ | PROVED (standard) |
| EF-T1 | Barrier: arguments using only an Euler product with $\Lambda\ge0$, continuation to $\operatorname{Re}s>\theta$ with $\theta\in(\tfrac12,1)$, and their consequences cannot give a zero-free region wider than $a/\log t$, by transfer to the Diamond–Montgomery–Vorhauer Beurling system. The extrapolation "a proof must use the FE and the Euler product jointly" is **WITHDRAWN** (Vinogradov–Korobov is a counterexample). | PROVED relative to EXT-DMV |
| EF-N | **Lemma N.** If $g\ge0$, $g\not\equiv0$ and $\operatorname{supp}g\subset[u_1,\infty)$ with $u_1>0$, then $\operatorname{Re}G$ takes negative values on every vertical line (Fejér-kernel argument). Known; cf. Lamzouri's remark that no nonconstant entire kernel has $\operatorname{Re}K\ge0$. | PROVED; not new |
| EF-K | **Theorem K.** For the favorable-sign class $\mathcal M_+$ ($a_k\ge0$, completely monotone $g$, all zeros except the quadruple discarded by sign): a contradiction is possible only if $1-\beta_0<2/\bigl(V(\log(\gamma_0/2)-6.2536)\bigr)$, where $V>34.468305$ is Landau's constant. At $\gamma_0=3\cdot10^{12}$ this is $1-\beta_0<0.002664$. | PROVED for the class (re-checked in consolidation). The sharpness claim (matching Landau's $R_0=V/2$) relies on Mossinghoff–Trudgian's description: UNVERIFIED in detail. |
| EF-V | $V\approx34.49$ from an LP over cosine polynomials of degree ≤ 48 (`landau-lp/lp.py`) | NUMERICALLY TESTED; agrees with the published bracket |
| EF-D | **Lemma D.** No $t$-uniform bound on $\operatorname{Re}(-\zeta'/\zeta)(1+\eta+it)$ better than its value at $t=0$ (Dirichlet approximation) | PROVED (standard) |
| EF-Z | **Target Lemma Z.** Uniform bounds on $\operatorname{Re}(-\zeta'/\zeta)(1+\eta+ik\gamma_0)$ for $k\ge2$, using that $\gamma_0$ is a zero ordinate | **OPEN** |
| EF-H | Heuristic: a Jensen-type local lemma with coefficient $c$ gives $R_0=cV$, and $c\in(0.16,0.25)$ reproduces the published constants 5.6–8.5 | UNVERIFIED heuristic |

## Obstruction

The archimedean term $\tfrac12\log\gamma_0$ at the frequencies $k\gamma_0$ is cancelled in reality by the zeros near $k\gamma_0$. Controlling those zeros is Lemma Z, and Lemma D shows that no $t$-uniform bound can do it.

## Strongest surviving result

Theorem K: an exact description of how far the classical positivity class reaches. It reproduces Landau's 1908 constant and says nothing new about zeros.

## Literature

- Mossinghoff–Trudgian (arXiv:1410.3926): $V$ bounds and the history of $R_0$.
- Mossinghoff–Trudgian–Yang (arXiv:2212.06867): 5.558691.
- Bellotti–Trudgian–Yang (arXiv:2603.21490): 4.896, found later.
- Diamond–Montgomery–Vorhauer (Math. Ann. 2006).
