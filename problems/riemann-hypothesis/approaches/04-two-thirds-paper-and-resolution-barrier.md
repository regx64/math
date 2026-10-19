# 04 — The 2026 "two thirds" results and the resolution barrier

**Phases** P4 (2026-10-19 01:11, survey and candidate list), P4b (01:20, self-audit), P5 (01:22–01:37, mechanism read and barrier). Main conversation. **Normalization:** [notation §5](../notation-and-normalization.md). **Scope [M]/[D]:** method limits for pair-correlation certificates.

## P4 — literature survey (as found on 2026-10-19; see [../external-results.md](../external-results.md))

- Alpöge–Furman, arXiv:2608.13637, with the proof discovered by an internal Claude model:
  - at least $2/3$ of zeros are simple and on the line ($0.6725$ with the Montgomery–Taylor window);
  - at least $5/6$ are distinct;
  - the bandwidth-one ceiling is $\approx0.682$;
  - Lean formalization in `anthropics/formal-math/zeta23`.
- Lamzouri, arXiv:2609.02882: a simpler Hilbert-space proof, plus "≥ 88.76% simple or on the line".
- Later follow-ups (found in P6): Knausgård, arXiv:2610.08965 (67.35% / 83.9%); Wang, arXiv:2609.24167 (gain of $+6.7\cdot10^{-8}$) and arXiv:2609.07918 (short intervals, with an automated-review objection about conjugation invariance).
- Bellotti–Trudgian–Yang, arXiv:2603.21490: zero-free region $1/(4.896\log t)$.
- Goldston–Suriajaya, arXiv:2511.20059; BGST, arXiv:2501.14545 (box assumption, method fails for $b\ge4.2$).
- de Bruijn–Newman $\Lambda\le0.1787854$: claimed on a blog, not refereed.

## P4 → P4b — candidate approaches A–F: WITHDRAWN as "new ideas"

Six candidates were proposed in P4:
- A: Weil–HS zero density
- B: sieve upper bounds beyond bandwidth one
- C: height-localized rank–trace
- D: Stechkin + smoothing method limit
- E: detection lemma in rank–trace language
- F: Connes–Consani support extension

When the user asked, P4b's self-audit found that none was a verified new idea: B and C were directions the paper itself points to, D was routine, E a repackaging, F Connes' own programme, and A had not been checked against prior art. The ideas had come from abstracts only. **Status: WITHDRAWN as novelty claims.** They remain as directions.

## P5 — the paper's mechanism (verified from the Lean source and the paper's §3, §4, §7.2)

**Rank–trace inequality** (Lean `rank_trace_ineq`, $c=2$):
$$r\ge2\operatorname{tr}P+4\operatorname{tr}Q-4b-\|P+Q\|_{HS}^2 .$$
On-line zeros give rank-one PSD blocks. Off-line pairs give signature-$(1,1)$ blocks.

**Ceiling law** (`PairCeiling/LawN256.lean`):
- a 256-periodic law; all points lie on the line, with marks in $\{1,2\}$;
- its simple-point fraction is $p_0=0.68182868746\ldots$;
- `ceiling_law256` bounds every bandwidth-one certificate's value by $p_0+0.824|r(1)|+2.55\cdot10^{-6}(\cdots)$, **modulo the hypothesis `EnclOK`**, which was certified outside Lean by interval arithmetic.

## Resolution barrier (P5)

| ID | Statement | Status |
|---|---|---|
| RES-1 | **Deformation identity.** Splitting each double point $x$ into $x\pm i\Delta$ gives $A_\Delta(\alpha)=A(\alpha)+(2\cosh2\pi\alpha\Delta-2)\sum_{\text{doubles}}e^{2\pi i\alpha x}$, with $S_\Delta=\lvert A_\Delta\rvert^2/N$ real. | PROVED; numerically checked (`resolution-barrier/resolution.py`: agreement to $5\cdot10^{-15}$, change of order $\Delta^2$) |
| RES-2 | **On-line ceiling.** Every bandwidth-one certificate that is valid for the *on-line* count (with multiplicity, or distinct), against configurations that may contain off-line pairs, has value at most $0.6818287+0.824\lvert r(1)\rvert+2.55\cdot10^{-6}(\cdots)$. | CONDITIONAL on `EnclOK` and on defining validity through the analytic form factor $\lvert A\rvert^2/N$ |
| RES-3 | **Finite Δ.** For "the fraction within normalized distance $<\Delta$", the value is at most $p_0+\text{stab}+\lVert r\rVert_\infty(10.385c+20.363c^2)$ with $c=2\cosh2\pi\Delta-2$. Constants re-checked in consolidation: $\sum s_j\le1.32395$, $\mathbb E d_c^2\le5212.9$. | CONDITIONAL (`EnclOK`) |
| RES-4 | **General principle.** For certificate classes whose data are uniformly continuous in zero positions, the on-line ceiling is at most the odd-multiplicity ceiling; so 100% on-line forces 100% simple. | SKETCHED (the meta-statement is not formalized) |

**Meaning.** A near-line pair and an on-line double zero give pair-correlation data that agree to $O(\Delta^2)$. Bandwidth-one second-moment methods therefore cannot certify more than about 68.2% on-line either.

**Novelty.** Not found in the material read. §7 of 2608.13637 was read only in excerpt, so experts may regard this as known.

## P5 idea list (round 2) and outcomes

| Idea | Outcome |
|---|---|
| 1, 2: resolution barrier | became RES-1 to RES-4 |
| 3: sieve upper bounds beyond bandwidth one | probably blocked by the parity barrier (heuristic). The law's form factor beyond $\alpha=1$ is not public. |
| 4: hybrid with Levinson / mollifier data | became [05](05-mollified-moments-hybrid.md) |
| 5: Δ-weighted HS density | rejected: the naive version is wrong ($F(\alpha)=\alpha<1$ is a counterexample) |
