# E6 — audit of the Gram-to-Toeplitz reduction against the Lean source (phase P9, 2026-10-19 09:34 KST)

**Question.** Do the spacing-1 counterexample and Theorem C apply to the Gram matrix actually used in the formalized Alpöge–Furman paper, or only to an abstract model?

**Source.** The P9 reply in the main conversation. Lean source: `anthropics/formal-math`, subdirectory `zeta23`, commit `e1a4e65` (cloned 2026-10-19). Line numbers are listed in [formalization/README.md](../formalization/README.md).

## A. Source definitions checked

All of these were read in the Lean source; nothing here is taken from summaries.
- `paperFT f z = ∫ f(u) e^{izu} du`.
- `gammaOf ρ = (ρ−1/2)/i`, which is complex for off-line zeros.
- `reflect ρ = 1 − conj ρ`, with `mult_reflect`.
- Grid: $L=\lambda\log(T/2\pi)$, $h=2\pi/L$, $d=\lfloor LT/2\pi\rfloor$, $\tau_k=T+kh$.
- Window $\varphi(u)=\varrho((L/2-|u|)/w)$, $a=L^{-1}\int\varphi^2$; hat units $M/(aL^2)$.
- `Gz` sums over all zeros, `Az` over $\gamma\in I'=(T-\sqrt T,2T+\sqrt T]$, and `Ez = Gz − Az`.
- `blockA = Σ m • vecMulVec v v` — transpose; the source comment says "NOT conjugate-transpose".
- `blockP` covers all on-line zeros (simple and multiple); `blockQ` covers pairs only.
- `PaperInputs Z` = H-EF + H-RvM + cheb + MV + Gamma.
- Trace and HS values are **derived** through H-EF; they are not hypotheses on `Z`.

## B. Derivation (verified)

1. **Rescaling.** Substituting $u=L\xi$ gives
$$\hat u_\rho(k)=\int\psi_L(\xi)e^{2\pi i\xi(\zeta_\rho-k)}d\xi,\qquad \psi_L=\varphi(L\cdot)/\sqrt a,\quad \zeta_\rho=(\gamma_\rho-T)L/2\pi .$$
2. **The pair.** For $\rho=\tfrac12+\delta+it$: $\gamma_\rho=t-i\delta$, so $\zeta=x-i\Delta$ with $\Delta=\delta L/2\pi$. **Δ enters the vectors.** The complex-frequency vector *is* the paper's vector.
3. **Compression.** $Q=P_\Gamma\,\mathbb G_F\,P_\Gamma$ exactly (Lemma 0 of [theorem-A-family](theorem-A-family.md)).
4. **Toeplitz form.** Under $\ell^2(\mathbb Z)\cong L^2[-\tfrac12,\tfrac12]$ followed by reflection, with ψ even:
$$x^*\mathbb G_Fx=\langle X,KX\rangle,\qquad K(\eta,\xi)=\psi(\eta)\psi(\xi)A(\xi-\eta),\qquad A(\beta)=\sum_\rho m_\rho e^{2\pi i\beta\zeta_\rho}.$$
   **The transpose is essential.** With an adjoint, every term would be PSD.
5. **Infinite lattice.** Entrywise Poisson summation (Theorem A).
6. **The first point E5B glossed over.** $Z(I')$ is finite, so an infinite-family statement does not apply directly. This is what Theorem A″ resolves.

## C–E. Verdicts

| Item | Verdict |
|---|---|
| Theorem A | VALID for infinite families (and the periodic model); a lemma, not a statement about the paper's finite matrix. |
| Theorem A′ | Identity VALID. Constant "uniform in d" **WITHDRAWN**: for $\psi_L$, $B\asymp e^{\pi\Delta}L/w$. |
| Theorem A″ | New. PROVED; it applies to the paper's finite matrix, and the bound is uniform in $L$. |
| Theorem C | Covers [D] configurations only. It satisfies the `ZeroConfig` axioms, H-RvM, `BlockInputs` and `TailInputs`, plus trace/HS data computed directly from $Z$. It **violates H-EF** and the unconditional Montgomery/BGST pair correlation. It is not [PI] and not [ζ]. |

**Classification of Theorem C:**

| Category | Covered? |
|---|---|
| Abstract matrix counterexample | yes |
| Counterexample to inferences that use only the stated numerical data | yes (SKETCHED: HS interface terms) |
| Configuration satisfying all of `PaperInputs` | no |
| Actual zeta zeros | no |

## F. Consequences

- AC over arbitrary finite families: REFUTED [M].
- AC over H-RvM configurations: REFUTED [D].
- AC over `PaperInputs` configurations: not refuted. Any proof of it must use H-EF beyond the trace and HS moments.
- Theorem NL: unproved, and not derivable from Theorem S's inputs (SKETCHED, inherits C).

## G. Minimal repair proposed

1. State AC relative to an explicit admissible class.
2. Use hat units, $\psi_L$, $\lambda=1$ and the $I'$ margins.
3. Add the open-band pair-correlation constraint, which is a consequence of `PaperInputs`. This gives **AC_F**, which is OPEN ([AC-F-open-problem.md](AC-F-open-problem.md)).

## Re-audit notes added during consolidation (2026-10-19 10:15)

- In A″ the indicator constant can be $\sinh(\pi\Delta)/\pi$; E6 stated $\cosh(\pi\Delta)/\pi$, which is valid but loose.
- A″ requires $C\subseteq\Gamma$ and consecutive lattice positions; both are now stated explicitly.
- "H-EF determines the zero multiset uniquely" was asserted as standard. It is not written out, so it is **UNVERIFIED** (claim AC-HEF).
- E6 also found that the paper's formal rank–trace lemma is parametrized by $c>0$ (`rank_trace_ineq`, `LinAlg/RankTrace.lean:163`):
$$c\operatorname{tr}P-\tfrac{c^2}4r+2c\operatorname{tr}Q-c^2b\le\|P+Q\|_F^2 .$$
  RT+ is the $c=2$ case with the slack terms kept.
