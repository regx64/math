# Open questions

These are ranked by how directly they bear on the project's live line, the near-line density question for bandwidth-one methods. All are OPEN. None was worked on during consolidation.

## 1. AC_F — does the full open-band pair correlation exclude far pairs? (claim AC-F)

**Question.** Is there $c>0$ such that every configuration with H-RvM and $S(\alpha)=\alpha+o(1)$ on compacts of $(0,1)$ pays negative mass $\operatorname{tr}Q^{\mathrm{pairs}}_-\ge c\sum(S_\psi(\Delta_k)-1)-o(N)$?

**First test.** The feasibility LP in [AC/AC-F-open-problem.md](AC/AC-F-open-problem.md):
- pair one spacing-1 pair cluster with a periodic on-line law;
- ask whether the total form factor can equal α.

**Why it matters.**
- If feasible: no bandwidth-one second-moment argument gives any near-line density bound.
- If infeasible: the dual certificate is the missing rigidity.

**Prerequisite.** Theorem C should first be moved from SKETCHED to PROVED; see the recommended next action in the [README](README.md).

## 2. Lemma Z — the frequencies $k\gamma_0$ (claim EF-Z)

**Question.** Can one bound $\operatorname{Re}(-\zeta'/\zeta)(1+\eta+ik\gamma_0)$ for $k\ge2$ better than the $t$-uniform bound, using only that $\gamma_0$ is the ordinate of a zero?

**Why it matters.** Lemma D shows that the uniform bound is optimal, so any gain must come from the arithmetic of $\gamma_0$. Without such a gain, the classical positivity method stays at Landau's constant (Theorem K).

## 3. Detection lemma DL (claim WEIL-DL)

**Question.** Does an off-line zero at height $t_0$ force $W(f*f^*)<0$ for some $f$ supported in $[-a,a]$ with $a\le C_0\log t_0$, under a local separation hypothesis?

**Why it matters.** Below the threshold $e^{2a}\approx(\log t_0)^2$, positivity is automatic (WEIL-COMB), so it carries no information. A detection lemma at logarithmic support would turn Weil positivity in a restricted regime into a zero-free statement.

## 4. Mollified pair correlation / near-line density with tiny constants (claims HYB-2, HYB-4)

**Question.** Can one prove $E=\sum_{\text{off-line}}\lvert\zeta'B\rvert^2\le10^{-4}NL^2$? Equivalently, can one prove a near-line zero-density estimate at normalized distances $10^{-3}$–$1$ with very small constants?

**Why it matters.** The transfer lemma H2 then certifies more than 68.2% simple zeros, which is beyond the resolution barrier (RES-2) of pair-correlation methods.

## 5. Ground state: cluster-level real zeros, or weak transform convergence (claims GS-3, GS-4)

**Question.** Is there a real-zeros theorem for the cluster of near-zero eigenvalues of $A_\lambda$, rather than for the ground state alone? Or a transform-convergence statement weaker than $L^2$-weighted, for example via Connes–Consani–Moscovici determinants?

**Why it matters.** Proposition C shows that every $L^2$-weighted version is as strong as RH. Only a genuinely weaker convergence notion could give leverage.

## Lower-priority items recorded elsewhere

- **AC-HEF.** Write out why H-EF pins down the zero multiset; or find a counterexample within `PaperInputs`.
- **AC-S.** Line-by-line assembly of Theorem S with the slack kept.
- **WEIL-P.** Is $\lvert\lambda_{\min}(a)\rvert\le\lambda_{\max}(a)$?
- **RES-4.** Formalize the resolution principle.
- **EF-K sharpness.** Check against Mossinghoff–Trudgian §2.
- **JEN-5.** Re-derive the induction theorem.
- **GS-1, GS-3.** Audit them.
