# Claims and status

This is the central ledger. Every mathematical claim made during the project has one entry. The file each claim came from may say more; **where they differ, this file governs.**

## Status labels

| Label | Meaning in this archive |
|---|---|
| PROVED | A complete paper-level proof exists in this archive and was re-checked by hand during consolidation (2026-10-19), unless the entry says otherwise. Not machine-checked. |
| FORMALLY VERIFIED | A Lean theorem exists **and** a build in this project confirmed it. **No claim currently has this status** (no Lean build was possible). |
| NUMERICALLY TESTED | Supported by computation only. Re-run results are recorded in [experiments/README.md](experiments/README.md). |
| CONDITIONAL | Proved assuming a named hypothesis that is not established. |
| SKETCHED | The argument is given, but at least one step is not written out or not re-checked. |
| OPEN | Neither proved nor refuted. |
| REFUTED | Shown false, with a counterexample at the stated scope. |
| WITHDRAWN | Retracted, because of an error, a non-uniformity, or because it was not new. |
| UNVERIFIED | Stated, but not checked in this project. This includes external statements taken from summaries and assessments or heuristics. |

## Scope tags (never promote across them)

- **[M]** matrices, or abstract families of points;
- **[D]** abstract zero configurations under selected constraints (`ZeroConfig` + H-RvM + `BlockInputs`/`TailInputs` + chosen numerical data);
- **[PI]** configurations satisfying the full `PaperInputs`, including H-EF;
- **[ζ]** the actual zeros of ζ.

A result at [M] or [D] says nothing about [PI] or [ζ] unless the entry says so explicitly.

## Summary

| ID | Short statement | Status | Scope |
|---|---|---|---|
| BASE-1 | Consequences of a hypothetical off-line zero | PROVED rel. EXT | [ζ] |
| BASE-2 | Admissible region $\mathcal C$ nonempty; FE + growth alone insufficient (Davenport–Heilbronn) | PROVED (nonempty) / UNVERIFIED citation | [ζ] |
| BASE-3 | RH is $\Pi^0_1$ | UNVERIFIED | — |
| EF-L1 | Compact-support explicit formula | PROVED (standard) | [ζ] |
| EF-L2 | Positivity inequality | PROVED | [ζ] |
| EF-L3 | Pole dominance | PROVED | [ζ] |
| EF-L4 | Zero-sum bound / "dlVP width" | WITHDRAWN | — |
| EF-L5 | Reflection invariance | PROVED | [ζ] |
| EF-L6 | Landau's theorem | PROVED (standard) | [ζ] |
| EF-T1 | Beurling barrier at width $a/\log t$ | PROVED rel. EXT-DMV; extrapolation WITHDRAWN | method |
| EF-N | Lemma N | PROVED | — |
| EF-K | Theorem K (favorable-sign class) | PROVED; sharpness UNVERIFIED | method |
| EF-V | $V\approx34.49$ (LP) | NUMERICALLY TESTED | — |
| EF-D | Lemma D | PROVED | [ζ] |
| EF-Z | Lemma Z | OPEN | [ζ] |
| EF-H | Jensen-type heuristic for $R_0$ | UNVERIFIED | — |
| WEIL-1 | Guinand–Weil normalization | NUMERICALLY TESTED | [ζ] |
| WEIL-2 | $S_{\mathrm{low}}\ge0$ | PROVED rel. EXT-PT | [ζ] |
| WEIL-3 | Tail bound | PROVED rel. EXT-TR | [ζ] |
| WEIL-AP | Almost positivity | PROVED rel. EXT | [ζ] |
| WEIL-Q | Quadruple contribution | SKETCHED | [ζ] |
| WEIL-ARCH | Archimedean lower bound | SKETCHED | [ζ] |
| WEIL-P | One-sided prime bound | PROVED (one-sided); two-sided UNVERIFIED | — |
| WEIL-λ | Jump of $\lambda_{\max}$ | PROVED | — |
| WEIL-THR | $e^{2a}\ge67$ | PROVED (finite computation) | [ζ] |
| WEIL-COMB | Combined inequality | SKETCHED | [ζ] |
| WEIL-λnum | $\lambda_{\max}\approx0.55e^a$, threshold ≈ 580 | NUMERICALLY TESTED | — |
| WEIL-CC | Dictionary with Connes–Consani | partly UNVERIFIED | — |
| WEIL-DL | Detection lemma | OPEN | [ζ] |
| LIT-AF | Candidates A–F as new ideas | WITHDRAWN | — |
| RES-1 | Deformation identity | PROVED | [M] |
| RES-2 | On-line ceiling | CONDITIONAL (`EnclOK`) | method |
| RES-3 | Finite-Δ ceiling | CONDITIONAL (`EnclOK`) | method |
| RES-4 | General resolution principle | SKETCHED | method |
| HYB-0 | Levinson's bound adds nothing | PROVED | method |
| HYB-1 | Scalar moments useless (H1) | PROVED | [D] |
| HYB-2 | Transfer lemma (H2) | PROVED | [D]→[ζ] conditional |
| HYB-3 | $\lvert\zeta'B\rvert^2$ heuristic | UNVERIFIED | — |
| HYB-4 | Mollified pair correlation assessment | UNVERIFIED | — |
| AC-B | Lemma B (pair spectrum) | PROVED (bi-infinite) | [M] |
| AC-RT+ | RT+ | PROVED | [M] |
| AC-S | Theorem S ($2\operatorname{tr}Q'_-$ form) | SKETCHED | [D]/[PI] |
| AC-S-slack | $(\lambda-2)^2$ slack in Theorem S | WITHDRAWN | — |
| AC-S-pairs | Pair corollary | SKETCHED | [D]/[PI] |
| AC-conj | AC, unrestricted | REFUTED | [M], [D] |
| AC-c012 | "$c\approx0.12$" | WITHDRAWN | — |
| AC-sp1 | Dismissal of the spacing-1 cancellation | WITHDRAWN | — |
| AC-NL | Theorem NL | WITHDRAWN | — |
| AC-Sel | "Better than Selberg" | WITHDRAWN | — |
| AC-L0 | Compression is exact | PROVED | [M] |
| AC-L1 | Single-vector decay | PROVED | [M] |
| AC-A | Theorem A | PROVED | [M] infinite |
| AC-A′ | Theorem A′ constant | identity PROVED; constant WITHDRAWN | [M] |
| AC-A″ | Theorem A″ | PROVED | [M] |
| AC-B2 | Theorem B ($e^{\pi\Delta}-1$) | PROVED (periodic) / SKETCHED | [M] |
| AC-ρ | Closed form $\rho(s,\Delta)$ | PROVED (periodic); continuum NUMERICALLY TESTED | [M] |
| AC-C | Theorem C | SKETCHED | [D] |
| AC-C-thr | Thresholds 0.2561 / 0.2944 / 0.3075 | NUMERICALLY TESTED (bulk) | [D] |
| AC-C-cons | Consequences of C for AC/NL | SKETCHED (inherits C) | [D] |
| AC-adm | Admissibility variants | mixed (see entry) | [D] |
| AC-HEF | H-EF determines the zero multiset | UNVERIFIED | [PI] |
| AC-F | AC_F | OPEN | [D] + pair correlation |
| AC-LP | Feasibility LP | OPEN (proposal) | — |
| LEAN-1 | `rank_trace_ineq` | UNVERIFIED build; statement read | formal |
| LEAN-2 | `blockInputs` for every ZeroConfig | UNVERIFIED build; statement read | formal |
| LEAN-3 | `eventually_tailInputs` needs only local count | UNVERIFIED build; statement read | formal |
| LEAN-4 | Poisson lemmas for real γ only | source fact (read) | formal |
| LEAN-5 | `ceiling_law256` conditional on `EnclOK` | UNVERIFIED build; statement read | formal |
| LEAN-6 | Headline 2/3 theorem hypothesis-free | UNVERIFIED (upstream claim) | [ζ] |
| GS-1 … GS-6 | Ground-state programme | see entries | [ζ] |
| JEN-1 … JEN-7 | Jensen interlacing | see entries | — |

---

## Detailed entries

Fields: **Statement** · **Assumptions/scope** · **Status** · **Evidence/dependencies** · **Source** · **Caveats** · **Next step**.

### Baseline ([approaches/01](approaches/01-contradiction-baseline.md))

**BASE-1.**
- **Statement.** If $\zeta(s_0)=0$ with $s_0=\sigma_0+it_0$ and $\sigma_0\ne\tfrac12$ nontrivial, then: $0<\sigma_0<1$; $t_0\ne0$; $s_0,\bar s_0,1-s_0,1-\bar s_0$ are four distinct zeros; $|t_0|>3\cdot10^{12}$; and $\sigma_0<1-c(\log t_0)^{-2/3}(\log\log t_0)^{-1/3}$.
- **Scope.** [ζ].
- **Status.** PROVED relative to EXT-PT and EXT-VK.
- **Evidence.** Standard facts.
- **Source.** P0 reply.
- **Caveats.** The Ford constant 1/57.54 is UNVERIFIED. The exact Platt–Trudgian height was recalled, not fetched.
- **Next.** Fetch Platt–Trudgian and Ford for the exact constants.

**BASE-2.**
- **Statement.** The region $\mathcal C$ of [01](approaches/01-contradiction-baseline.md) is nonempty. The Davenport–Heilbronn function satisfies an FE of the same type and has zeros with $\operatorname{Re}s>1$.
- **Scope.** [ζ] (nonemptiness); a citation (DH).
- **Status.** Nonemptiness PROVED (trivial). The DH fact is UNVERIFIED (recalled).
- **Next.** Cite a source for DH.

**BASE-3.**
- **Statement.** RH is $\Pi^0_1$.
- **Status.** UNVERIFIED.
- **Next.** Cite Lagarias, or the standard arithmetization.

### Smoothed explicit formula ([approaches/02](approaches/02-smoothed-explicit-formula.md))

**EF-L1.**
- **Statement.** For $g\in C^2$ with $\operatorname{supp}g\subset[u_1,u_2]$, $u_1>0$, and every $s$: $\sum\Lambda(n)n^{-s}g(\log n)=G(1-s)-\sum_\rho m_\rho G(\rho-s)-\sum_mG(-2m-s)$, all sums absolutely convergent.
- **Scope.** [ζ].
- **Status.** PROVED (standard contour shift).
- **Caveats.** False for non-compact $g$.

**EF-L2.** Positivity of the weighted sum with $P\ge0$ and $g\ge0$. PROVED. Elementary.

**EF-L3.**
- **Statement.** If $\bar u(1-\beta_0)\ge\log4$ then $a_1[G(0)+G(1-2\beta_0)]<a_0G(1-\beta_0)$.
- **Status.** PROVED (Fejér–Egerváry and Jensen).
- **Caveats.** A contradiction also needs $a_1>0$ and $a_k\ge0$.

**EF-L4.**
- **Statement as made.** A zero-sum bound giving a de la Vallée Poussin width.
- **Status.** WITHDRAWN.
- **Reason.** It used a zero count $\ll Y\log T$ in windows of width $Y<1$, which is not known.

**EF-L5.** The reflection identity at $\sigma=1-\beta_0$. PROVED.

**EF-L6.** Landau: $\psi(x)-x=O(x^a)$ implies no zeros with $\operatorname{Re}s>a$. PROVED (standard).

**EF-T1.**
- **Statement.** Arguments using only an Euler product with $\Lambda\ge0$ and continuation to $\operatorname{Re}s>\theta$ cannot give a zero-free region wider than $a/\log t$.
- **Status.** PROVED relative to EXT-DMV. The extrapolation "a proof must use the FE and the Euler product jointly" is WITHDRAWN.
- **Caveats.** "Arguments using only" is a meta-statement. It is made precise only as "the conclusion fails for the DMV system".

**EF-N.**
- **Statement.** If $g\ge0$, $g\not\equiv0$ and $\operatorname{supp}g\subset[u_1,\infty)$ with $u_1>0$, then $\operatorname{Re}G$ takes negative values on every vertical line.
- **Status.** PROVED. Known, not new.

**EF-K.**
- **Statement.** In the class $\mathcal M_+$, a contradiction requires $1-\beta_0<2/\bigl(V(\log(\gamma_0/2)-6.2536)\bigr)$.
- **Scope.** Method class.
- **Status.** PROVED for the class (re-checked).
- **Evidence.** Re-derivation; `landau-lp/lp.py` for $V$.
- **Caveats.** The sharpness (the match with Landau's $R_0=V/2$) is UNVERIFIED in detail.
- **Next.** Read Mossinghoff–Trudgian §2 against the constant 6.2536.

**EF-V.**
- **Statement.** The LP over cosine polynomials of degree ≤ 48 gives $V\approx34.49$.
- **Status.** NUMERICALLY TESTED. Re-run: see experiments.
- **Caveats.** An LP upper estimate is not a certified bound.

**EF-D.** Lemma D. PROVED (Dirichlet approximation).

**EF-Z.**
- **Statement.** A uniform bound on $\operatorname{Re}(-\zeta'/\zeta)(1+\eta+ik\gamma_0)$ for $k\ge2$, using that $\gamma_0$ is a zero ordinate.
- **Status.** OPEN.

**EF-H.** Heuristic $R_0=cV$ with $c\in(0.16,0.25)$. UNVERIFIED.

### Weil form ([approaches/03](approaches/03-weil-form-height-split.md))

**WEIL-1.**
- **Statement.** With the normalization of [notation §6](notation-and-normalization.md), the Guinand–Weil identity holds numerically for the tested $g$, using 415 zeros.
- **Status.** NUMERICALLY TESTED.
- **Evidence.** `weil-identity/`, re-run 2026-10-19.
- **Caveats.** A numerical check of a known identity's normalization; not a proof of anything new.

**WEIL-2.** PROVED relative to EXT-PT.

**WEIL-3.**
- **Statement.** $\lvert S_{\mathrm{high}}(T)\rvert\le\frac2\pi e^a\lVert g''\rVert_1(\log T+1)/T$ for $T\ge10$.
- **Status.** PROVED relative to EXT-TR.
- **Caveats.** On $[10,10^{16}]$ the margin was checked numerically (minimum 0.62).

**WEIL-AP.**
- **Statement.** $W(f*f^*)\ge-1.2618\cdot10^{-11}a\,e^a\lVert f'\rVert_2^2$ for every real $f\in C^2_c([-a,a])$.
- **Scope.** [ζ].
- **Status.** PROVED relative to EXT-PT and EXT-TR (re-checked).

**WEIL-Q, WEIL-ARCH, WEIL-COMB.** SKETCHED. Constants were not re-derived.

**WEIL-P.**
- **Statement.** $P(g)\le2\lambda_{\max}(a)g(0)$.
- **Status.** One-sided bound PROVED. The two-sided $\lvert P\rvert$ bound written in P3 is UNVERIFIED.
- **Caveats.** Only the one-sided bound is used.

**WEIL-λ.** PROVED.

**WEIL-THR.** $S(66)<13.4459<S(67)$. PROVED (exact finite computation; re-run in `prime-threshold/`).

**WEIL-λnum.**
- **Status.** NUMERICALLY TESTED.
- **Caveats.** $\lambda_{\max}$ was computed by discretization. It is not certified.

**WEIL-CC.**
- **Status.** The support and pole matches are checked. The "vanishing at 0" condition is UNVERIFIED.

**WEIL-DL.** The detection lemma. OPEN.

### Literature and resolution ([approaches/04](approaches/04-two-thirds-paper-and-resolution-barrier.md))

**LIT-AF.**
- **Statement.** Candidates A–F were new approaches.
- **Status.** WITHDRAWN (P4b).

**RES-1.**
- **Statement.** Splitting each double point $x$ into $x\pm i\Delta$ gives $A_\Delta(\alpha)=A(\alpha)+(2\cosh2\pi\alpha\Delta-2)\sum_{\text{doubles}}e^{2\pi i\alpha x}$.
- **Scope.** [M].
- **Status.** PROVED (direct; numerical check `resolution.py`).

**RES-2.**
- **Statement.** Every bandwidth-one certificate valid for the on-line count has value $\le0.6818287+0.824\lvert r(1)\rvert+2.55\cdot10^{-6}(\cdots)$.
- **Status.** CONDITIONAL on `EnclOK`, and on defining validity through $\lvert A\rvert^2/N$.
- **Dependencies.** LEAN-5 plus RES-1.

**RES-3.** CONDITIONAL on `EnclOK`. The constants 1.32395 and 5212.9 were re-checked.

**RES-4.**
- **Status.** SKETCHED.
- **Caveats.** A meta-statement, not formalized.

### Hybrid ([approaches/05](approaches/05-mollified-moments-hybrid.md))

**HYB-0, HYB-1, HYB-2.** PROVED.
- HYB-2's thresholds are arithmetic (`hybrid.py`).
- HYB-2 transfers to [ζ] only if one can bound $E$, which is not done.

**HYB-3, HYB-4.** UNVERIFIED.

### AC trail ([AC/](AC/README.md))

**AC-B (Lemma B).**
- **Statement.** For ψ even, real, supported in $[-\tfrac12,\tfrac12]$ with $\int\psi^2=1$, and any $z\in\mathbb C$: $\sum_{k\in\mathbb Z}v_z(k)^2=1$ (transpose square, not modulus). A pair block has eigenvalues $1+S_\psi(\Delta)$ and $1-S_\psi(\Delta)$.
- **Scope.** [M], bi-infinite grid.
- **Status.** PROVED.
- **Caveats.** On a finite grid there is edge leak. The upstream Poisson lemma covers real γ only (LEAN-4).

**AC-RT+.**
- **Statement.** See [theorem-S-and-NL](AC/theorem-S-and-NL.md).
- **Scope.** [M].
- **Status.** PROVED (re-derived twice).
- **Dependencies.** The von Neumann trace inequality.
- **Caveats.** The slack terms are not formalized (LEAN-1 covers the slack-free part).

**AC-S.**
- **Statement.** $2\operatorname{tr}(Q'_-)\le(R(\psi)-1)N-2p-m_2+o(N)$.
- **Scope.** Configurations with the paper's trace/HS data. Those data are derived from [PI]; the inequality uses only them.
- **Status.** SKETCHED.
- **Dependencies.** AC-RT+, TailInputs, trace and HS asymptotics.
- **Next.** Re-derive the assembly with the slack kept, line by line against `Assembly.lean`.

**AC-S-slack.** The $\sum(\lambda-2)^2$ term. WITHDRAWN (not stable in trace norm).

**AC-S-pairs.** $\operatorname{tr}Q^{\mathrm{pairs}}_-\le\tfrac12[(R-1)N-2p+m_2]+o(N)$. SKETCHED (inherits AC-S).

**AC-conj.**
- **Statement as made.** For all finite pair families with $\Delta_k\le\Delta_0$: $\operatorname{tr}Q^{\mathrm{pairs}}_-\ge c\sum(S_\psi(\Delta_k)-1)$.
- **Status.** REFUTED at [M] by AC-A″ (finite spacing-1 clusters: ratio $O(\sqrt{\log\ell/\ell})$), and at [D] by AC-C.
- **Caveats.** Not refuted at [PI] or [ζ].

**AC-c012.** WITHDRAWN. A finite-size artifact; the exact lattice value at Δ = 3 is 0.00152.

**AC-sp1.** WITHDRAWN.

**AC-NL.** WITHDRAWN. Its premise is refuted, it is not derivable from AC-S's data (AC-C), and Jutila is stronger anyway.

**AC-Sel.** WITHDRAWN.

**AC-L0.** $Q=P_\Gamma\mathbb G_FP_\Gamma$. PROVED.

**AC-L1.** $\lvert\hat g(s)\rvert\le c/\lvert s\rvert$ with the constants in [theorem-A-family](AC/theorem-A-family.md). PROVED. The $\psi_L$ constant is uniform in $L$ via $a\ge\tfrac12$.

**AC-A.**
- **Statement.** The bi-infinite lattice Gram matrix is $2\,\mathrm{Toeplitz}(\psi^2)\succeq0$, independent of Δ.
- **Scope.** [M], infinite families.
- **Status.** PROVED.
- **Evidence.** Numerically, ratio 0 to $10^{-15}$ (E2a).

**AC-A′.**
- **Status.** The identity is PROVED. The constant $\zeta(3)B^2/4\pi^4$ "uniform in $d$" is WITHDRAWN for $\psi_L$.

**AC-A″.**
- **Statement.** For $C\subseteq\Gamma$ consecutive with $\lvert C\rvert=\ell$: $\operatorname{tr}Q_-\le4\beta+2\sqrt{\ell S\beta}$ and $\beta\le2c^2(2+\log\ell)$.
- **Scope.** [M].
- **Status.** PROVED (re-derived step by step; constants checked against E6 numbers).
- **Caveats.** Multiplicity 1, lattice positions. Clusters extending beyond Γ need A′'s identity.
- **Next.** Formalize in Lean (would be the first FORMALLY VERIFIED item).

**AC-B2.**
- **Statement.** Theorem B: $\operatorname{tr}Q_-/\#\text{pairs}\le e^{\pi\Delta}-1$ for spacing-2 lattices.
- **Status.** PROVED in the periodic model. The continuum and finite-segment versions are SKETCHED.

**AC-ρ.** PROVED in the periodic model. The continuum limit is NUMERICALLY TESTED (e2).

**AC-C.**
- **Statement.** There are [D]-configurations (`ZeroConfig`, H-RvM, `BlockInputs`, `TailInputs`, $\operatorname{tr}\hat A=N(1+o(1))$, $\lVert\hat A\rVert_F^2\le RN$) with an off-line pair fraction up to the thresholds, and $\operatorname{tr}Q^{\mathrm{pairs}}_-=o(N)$.
- **Scope.** [D] **only**. It violates H-EF and BGST pair correlation.
- **Status.** SKETCHED. The interface HS and trace-edge estimates are not written out; the H-RvM tuning is sketched.
- **Dependencies.** AC-A″, LEAN-2, LEAN-3.
- **Next.** Write the interface and edge estimates.

**AC-C-thr.** Bulk thresholds 0.2561 / 0.2944 / 0.3075 from exact formulas plus quadrature (`e4c_exact.py`). NUMERICALLY TESTED; re-run.

**AC-C-cons.** No inequality valid on all [D]-admissible data can yield NL from AC-S. SKETCHED.

**AC-adm.**
- Density ≤ 1: not refuted; upper bound on $c$ PROVED via AC-B2.
- Bounded local excess: UNVERIFIED for ζ.
- Known local count allows clusters of length $\log T$: PROVED (elementary).
- Translation averaging: useless, PROVED.

**AC-HEF.** "H-EF pins down the zero multiset." UNVERIFIED (asserted as standard; not written).

**AC-F.**
- **Statement.** See [AC-F-open-problem](AC/AC-F-open-problem.md).
- **Status.** OPEN.

**AC-LP.** Feasibility LP. OPEN (a proposal only, not run).

### Formal (upstream) facts ([formalization/README.md](formalization/README.md))

For these entries the status describes **this project's** verification. "Statement read" means the declaration was found in source with the quoted statement. No build was run.

| ID | Statement | Status |
|---|---|---|
| LEAN-1 | `rank_trace_ineq` (`LinAlg/RankTrace.lean:163`) states $c\operatorname{tr}P-\tfrac{c^2}4r+2c\operatorname{tr}Q-c^2b\le\lVert P+Q\rVert_F^2$ | UNVERIFIED build; statement read |
| LEAN-2 | `blockInputs` (`ZeroSide/Final.lean:57`) gives `BlockInputs` for every `ZeroConfig` with valid params | UNVERIFIED build; statement read |
| LEAN-3 | `eventually_tailInputs` (`Tail.lean:651`) needs the local count plus window decay/conjugation facts, not H-EF | UNVERIFIED build; statement read |
| LEAN-4 | `hasSum_phiHatR_mul` / `_sq` are stated for real arguments | source fact (read) |
| LEAN-5 | `ceiling_law256` has hypothesis `EnclOK`, certified outside Lean; the certificate is not public | UNVERIFIED build; statement read |
| LEAN-6 | `two_thirds_simple_on_critical_line` is proved in `Solution.lean` by `Zeta23.thmB₀_mult`, with no hypotheses (upstream claim, comparator-checked per README) | UNVERIFIED (not rebuilt) |

### Ground state ([approaches/spectral-ground-state](approaches/spectral-ground-state.md))

| ID | Status |
|---|---|
| GS-1 | UNVERIFIED |
| GS-2 | SKETCHED. $y_*$ and $c_\infty$ re-computed: NUMERICALLY TESTED. |
| GS-3 | UNVERIFIED |
| GS-4 | inequality PROVED; consequence SKETCHED |
| GS-5 | assessment |
| GS-6 | UNVERIFIED |

All GS entries are scope [ζ]-directed but are not results about ζ.

### Jensen ([approaches/jensen-interlacing](approaches/jensen-interlacing.md))

| ID | Status |
|---|---|
| JEN-1 | PROVED (remark) |
| JEN-2 | PROVED |
| JEN-3 | PROVED |
| JEN-4 | PROVED for hyperbolicity (with multiplicity); root counts NUMERICALLY TESTED (exact sympy). Caveat (re-run): the example's $J_{d,n}$ have multiple zeros, so it does not refute propagation of *simple-zero* hyperbolicity. |
| JEN-5 | SKETCHED (the source calls it proved; not re-derived in consolidation) |
| JEN-6 | NUMERICALLY TESTED |
| JEN-7 | assessment |
