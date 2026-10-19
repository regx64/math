# Research ledger (chronological)

Times are KST from the conversation messages. Three claude.ai conversations in the project "리만 가설" are involved:
- **main**: this archive's primary source;
- **GS**: chat `de654dc8`, ground state;
- **JEN**: chat `15786f47`, Jensen polynomials.

Original claims are kept as they were made; later revisions are marked ⟶.

| # | When | Question | Idea / derivation | Result | Audit / correction | Current status | Notes |
|---|---|---|---|---|---|---|---|
| P0 | 10-18 23:51 (main) | Can a contradiction be derived from an off-line zero using established results? | Formalize RH; list constraints (FE, symmetry, Euler product, zero-free regions, density, numerics) | The admissible region $\mathcal C$ is nonempty; no contradiction | — | BASE-1 PROVED (rel. EXT); BASE-2 literature claim | [01](approaches/01-contradiction-baseline.md) |
| P1 | 10-18 23:57 (main) | "Genuine attempt" at a proof by contradiction | Smoothed explicit formula + positivity of Λ; L1–L6; barrier T1 via Beurling systems | Outcome B; claimed de la Vallée Poussin width | ⟶ P2: L4 invalid, width not derived | see P2 | [02](approaches/02-smoothed-explicit-formula.md) |
| P2 | 10-19 00:03–00:24 (main) | Audit L1–L6, T1; resume | Lemma N; Theorem K (favorable-sign class); LP for $V$; Lemma D; Lemma Z | Theorem K reproduces Landau's 1908 limit | L4 WITHDRAWN; T1 extrapolation WITHDRAWN | K PROVED (class); Z OPEN | [02](approaches/02-smoothed-explicit-formula.md) |
| GS | 10-19 00:38 (GS) | Perron–Frobenius ground state for Weil's operator | Operator $A_\lambda$; positivity improvement; prolate / Pólya approximation; Connes–van Suijlekom + Hurwitz | Sharp threshold $\lambda_*\approx1.151$; cluster collapse; circularity (Prop. C) | not re-audited here | mostly UNVERIFIED / SKETCHED | [spectral](approaches/spectral-ground-state.md) |
| JEN | 10-19 00:43 (JEN) | Recursive Jensen interlacing | Recurrences; interlacing ⇔ simple real roots; counterexample kernel | Reformulation of RH; backward propagation fails | normalization corrected in the source | JEN-2/3/4 PROVED; JEN-6 numerics re-run | [jensen](approaches/jensen-interlacing.md) |
| P3 | 10-19 00:28 (main) | Split Weil's form at height T | Guinand–Weil identity checked numerically; tail bound; localized test functions | Almost positivity; automatic-positivity threshold ($e^{2a}\ge67$) | ⟶ consolidation: $\lvert P\rvert$ bound only one-sided | WEIL-AP PROVED; DL OPEN | [03](approaches/03-weil-form-height-split.md) |
| P4 | 10-19 01:11 (main) | Latest results → new approaches | Survey of 2026 results; candidates A–F | list | ⟶ P4b (01:20): not new ideas | WITHDRAWN as novelty | [04](approaches/04-two-thirds-paper-and-resolution-barrier.md) |
| P5 | 10-19 01:22–01:31 (main) | What exactly limits the 2/3 method? | Read the Lean source and paper excerpts; split double points into near-line pairs | R1–R4 resolution barrier | — | RES-1 PROVED; RES-2/3 CONDITIONAL; RES-4 SKETCHED | [04](approaches/04-two-thirds-paper-and-resolution-barrier.md) |
| P6 | 10-19 01:37 (main) | Hybrid with Levinson / mollifier data | CGG moments; free-value model | H1 (scalar data useless), H2 (transfer lemma) | — | PROVED; H3 assessment only | [05](approaches/05-mollified-moments-hybrid.md) |
| P7 | 10-19 01:46 (main) | Use the rank–trace slack against far pairs | Lemma B, RT+, Theorem S, **AC**, Theorem NL | NL "with $c\approx0.12$" | ⟶ P8/P9 | AC REFUTED; NL WITHDRAWN | [AC/01](AC/01-original-conjecture.md) |
| P8 | 10-19 08:28 (main), "E5B" | Adversarial audit of AC | Exact lattice formulas; three implementations; segments; mixed configurations; adversary | AC false (spacing-1 lattice); Theorem C; $c\approx0.12$ was an artifact; Jutila | ⟶ P9: A′ constant non-uniform; C is [D] only | see AC/ | [AC/02](AC/02-E5B-audit.md) |
| P9 | 10-19 09:34 (main), "E6" | Does the reduction match the paper's Gram matrix? | Lean source audit; compression; Toeplitz form; block decomposition | Theorem A″; classification of C; AC_F | ⟶ consolidation: A″ constants tightened; H-EF uniqueness UNVERIFIED | A″ PROVED; C SKETCHED; AC_F OPEN | [AC/03](AC/03-E6-audit.md) |
| P10 | 10-19 10:15 | Consolidate into `regx64/math` | Archive, claim ledger, re-runs | this archive | — | — | [README](README.md) |
