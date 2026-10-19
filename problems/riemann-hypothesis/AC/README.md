# The AC line of attack (inertia slack → near-line zero density)

**One-line summary.** The idea was to keep the slack in the Alpöge–Furman rank–trace inequality, so that off-line zero pairs far from the critical line would be charged against the Hilbert–Schmidt budget. The key inequality AC turned out to be **false for arbitrary pair families** ([M]). The data used by Theorem S cannot rule out a positive proportion of far pairs ([D], SKETCHED). The restricted question AC_F, which adds the full pair correlation, is **OPEN**.

## Reading order

1. [01-original-conjecture.md](01-original-conjecture.md) — AC, Theorem S and Theorem NL exactly as first proposed (P7), with what happened to each.
2. [02-E5B-audit.md](02-E5B-audit.md) — the adversarial audit (P8): lattice counterexample, withdrawn constants, Theorem C.
3. [03-E6-audit.md](03-E6-audit.md) — the audit against the Lean source (P9): exact definitions, A″, classification of Theorem C.
4. Canonical statements and proofs:
   - [theorem-A-family.md](theorem-A-family.md) — Theorems A, A′, A″, B.
   - [theorem-C.md](theorem-C.md) — data-insufficiency.
   - [theorem-S-and-NL.md](theorem-S-and-NL.md) — RT+, Theorem S, the withdrawal of NL.
5. [AC-F-open-problem.md](AC-F-open-problem.md) — the open restricted conjecture and the proposed LP.

## Status at a glance

| Claim | Status | Scope |
|---|---|---|
| Lemma B (pair spectrum $\{1\pm S\}$) | PROVED (bi-infinite grid) | [M] |
| RT+ | PROVED | [M] |
| Theorem S ($2\operatorname{tr}Q'_-$ term) | SKETCHED | [D]→[PI] inputs |
| AC (unrestricted) | **REFUTED** | [M], [D] |
| Theorem A | PROVED | [M], infinite families |
| Theorem A′ constant | **WITHDRAWN** | — |
| Theorem A″ | PROVED | [M] |
| Theorem B | PROVED (periodic model) / SKETCHED | [M] |
| Theorem C | SKETCHED | [D] |
| Theorem NL | **WITHDRAWN** | — |
| "$c\approx0.12$" | **WITHDRAWN** | — |
| AC_F | **OPEN** | [D] with pair correlation |

Full fields for each claim: [../claims-and-status.md](../claims-and-status.md) (IDs `AC-*`).
