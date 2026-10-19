# AC_F — the restricted conjecture (OPEN)

**Status: OPEN.** No proof and no counterexample exist. Nothing on this page is an established result.

## Admissible class $\mathcal A_F$

Configurations (reflection-invariant multisets, $\lambda=1$ normalization) satisfying:
1. **H-RvM:** the main count $N(T,2T)=T\,\mathrm{ell1}/2\pi+O(\log T)$ and the local count $N(t,t+1)\le A_0\log(|t|+3)$;
2. **open-band pair correlation:** for every fixed compact $K\subset(0,1)$,
$$S(\alpha)=\frac{|A(\alpha)|^2}{N}=\alpha+o(1)\quad\text{uniformly for }\alpha\in K,\qquad A(\alpha)=\sum_\rho m_\rho e^{2\pi i\alpha z_\rho}.$$

**Interpretation of the limit.** Statements are asymptotic as $T\to\infty$. Constraint 2 is tested by band-limited test functions $r$ supported in $[-1,1]$. Such tests cannot see mass concentrating at the endpoint $\alpha=1$: a certificate with $r(1)=0$ weights a spike of width $1/\ell$ by $O(1/\ell)$. This is the "free row" exploited by the Alpöge–Furman ceiling law (`LawN256.lean`, `CeilingLaw256.lean`).

Constraint 2 is a consequence of `PaperInputs` (Montgomery 1973 made unconditional by BGST), so imposing it is legitimate. It is strictly weaker than H-EF.

## Conjecture AC_F

For a window ψ and $\Delta_0>0$ there are $c>0$ and $o(N)$ such that every configuration in $\mathcal A_F$ satisfies
$$\operatorname{tr}(Q^{\mathrm{pairs}}_-)\ \ge\ c\sum_{k:\,\Delta_1\le\Delta_k\le\Delta_0}\bigl(S_\psi(\Delta_k)-1\bigr)-o(N).$$
The exact form of the right-hand side is itself provisional. Theorem B suggests replacing $S-1$ by a quantity of size $e^{\pi\Delta}$.

## Why it is not settled by Theorems A″ and C

- **Theorem C** uses lattice regions, whose form factor is near 0 on most of $(0,1)$. They violate constraint 2.
- **Theorem A″** shows that a spacing-1 pair cluster costs $o(\ell)$ negative mass regardless of its surroundings. So the question reduces to whether the *rest* of the configuration can make the total form factor equal α.

## Proposed feasibility problem (future work, not carried out)

Fix $\lambda_1>0$. Does there exist a periodic marked on-line law of density $(1-2\lambda_1)/(1-\lambda_1)$ whose form factor, together with that of a spacing-1 pair cluster occupying a fraction $\lambda_1$ of the length, gives total $S(\alpha)=\alpha$ on compact subsets of $(0,1)$? Heuristically the cross terms are $O(e^{2\pi\Delta}/\sqrt N)$ in the bulk.

- **If feasible for some $\lambda_1>0$:** AC_F fails, and no bandwidth-one second-moment argument yields a near-line density bound at any fixed Δ.
- **If infeasible for all $\lambda_1>0$:** the LP dual certificate is the extra rigidity a repaired argument must use.

Possible tooling: the exact-rational 256-periodic LP framework of Alpöge–Furman §7.2. Their certificate file is not public ("available from the authors").

## Related open items

- **Lemma Z** ([approaches/02](../approaches/02-smoothed-explicit-formula.md)): bounds on $-\zeta'/\zeta$ at multiples of a zero ordinate.
- **The detection lemma DL** ([approaches/03](../approaches/03-weil-form-height-split.md)).
