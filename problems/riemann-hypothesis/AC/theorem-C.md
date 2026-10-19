# Theorem C — Theorem S's data cannot yield a near-line density bound

**Scope: [D] only.** This is a counterexample to *inferences* that use only certain numerical data. It is not a zero configuration satisfying `PaperInputs`, and it says nothing about actual zeta zeros.

**Overall status: SKETCHED.** The components and their statuses are listed below.

## Construction

Take $\lambda=1$, so that zeros have mean spacing 1 in grid units. Fix a fraction $\lambda_1\in(0,\tfrac12)$ and any $\Delta>0$. The construction lives in normalized coordinates over $I'$; the margins are filled with the same pattern.
- **Pair region:** a single cluster of $\ell=\lambda_1d$ pairs at consecutive integers, all at distance Δ. This is $2\ell$ zeros on length $\ell$, i.e. local density 2.
- **On-line region:** $d-2\ell$ simple on-line zeros, equally spaced at $s=(1-\lambda_1)/(1-2\lambda_1)$ on the remaining length.
- **Global count.** The count is $N=d(1+o(1))$. It must be adjusted to $T\cdot\mathrm{ell1}/2\pi+O(\log T)$ to meet H-RvM main; this is done by tuning $s$ (SKETCHED).

## What the construction satisfies

| Constraint | Satisfied? | Status / reason |
|---|---|---|
| `ZeroConfig` axioms (strip, reflection, multiplicity, local finiteness) | yes | trivial |
| H-RvM main count | yes, after tuning | SKETCHED |
| H-RvM local count $N(t,t+1)\le A_0\log(\lvert t\rvert+3)$ | yes, for $A_0$ of order $1/\pi$ | PROVED (density at most 2 in normalized units) |
| `BlockInputs` (block structure) | yes | formally proved upstream for **every** `ZeroConfig` (`ZeroSide/Final.lean:57`) |
| `TailInputs` | yes | upstream needs only the local count (`Tail.lean` `eventually_tailInputs`) |
| $\operatorname{tr}\hat A=N(1+o(1))$ | yes | SKETCHED: bulk via Lemma B (Poisson); edges not written out |
| $\|\hat A\|_F^2\le(R(\psi)-\eta)N$ | yes, for $\lambda_1$ below the thresholds below | bulk values: exact formulas evaluated by quadrature (NUMERICALLY TESTED); interface terms SKETCHED |
| $\operatorname{tr}(Q^{\mathrm{pairs}}_-)=o(N)$ | yes: $O(\sqrt{N\log N})$ | **PROVED** via Theorem A″ |
| **H-EF** (explicit formula) | **no** | the configuration's Gram matrix is not the prime-side matrix |
| Unconditional Montgomery/BGST pair correlation $F(\alpha)=\alpha+o(1)$ | **no** | lattice regions have $S(\alpha)\approx0$ on most of $(0,1)$ |

## Bulk HS (exact formulas)

- Pair lattice at spacing 1: Gram $=2\,\mathrm{Toeplitz}(\psi^2)$, so HS per unit length is $4\int\psi^4$, independent of Δ.
- Simple on-line lattice at spacing $s$: HS per unit length is $s^{-2}\int_{-1/2}^{-1/2+1/s}\bigl(\sum_n\psi^2(u_0+n/s)\bigr)^2du_0$.
- Mixed configuration: $\mathrm{HS}/N=4\lambda_1\int\psi^4+(1-\lambda_1)\,h(s)$.

Largest admissible $\lambda_1$ (script `e4c_exact.py`):

| Window | $R(\psi)$ | Maximal off-line fraction $2\lambda_1$ |
|---|---|---|
| indicator (the limit of the paper's $\psi_L$) | 1.33333 | 0.2561 |
| Montgomery–Taylor $\cos(\sqrt2\,\xi)$ | 1.33268 | 0.2944 |
| taper, ramp 0.1 | 1.40914 | 0.3075 |

For the paper's $\psi_L$, take $\lambda_1$ slightly below the indicator threshold; then $\mathrm{HS}<RN$ for all large $L$. **Equality** $\mathrm{HS}=RN$ can be reached by disordering the on-line part continuously: a lattice gives HS below $R$, a Poisson arrangement gives HS above $R$. This step is SKETCHED.

## What it demonstrates

- No inequality that holds for all [D]-admissible matrices can combine with Theorem S's inputs (rank–trace algebra, block structure, trace, HS, counts, tail) to bound the number of off-line pairs at fixed Δ by $o(N)$.
- In particular, AC with any $c>0$ fails on this class, and Theorem NL cannot be derived from Theorem S.

## What it does not demonstrate

- Anything about configurations satisfying H-EF, i.e. essentially the actual zeros. The claim that H-EF pins down the zero multiset is UNVERIFIED (claim AC-HEF).
- Anything about RH.
- Whether the **full** open-band form factor data exclude far pairs. That question is AC_F ([AC-F-open-problem.md](AC-F-open-problem.md)).

## Next verification step

Write out the interface estimate for $\|\hat A\|_F^2$ and the edge estimate for $\operatorname{tr}\hat A$ (Lemma 1 decay plus counting, as in A″). This would move Theorem C from SKETCHED to PROVED.
