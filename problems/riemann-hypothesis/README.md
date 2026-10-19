# Riemann Hypothesis — research archive

**Period:** 2026-10-18 23:51 – 2026-10-19 (KST). Work was done in three claude.ai conversations in the project "리만 가설". This archive was consolidated on 2026-10-19.

**Bottom line.**
- **RH was not proved.** No step of this project is evidence for or against RH.
- What exists is a set of method-limit results, at the scopes [M], [D] and method classes:
  - why the classical positivity method stops at Landau's constant;
  - where Weil positivity becomes informative;
  - why pair-correlation certificates cannot see near-line zeros (the resolution barrier);
  - why the inertia-slack idea AC fails without arithmetic input.
- Several earlier claims were **withdrawn** after audit, and are kept here marked as such.
- Nothing in this archive is FORMALLY VERIFIED. Paper-level proofs were re-checked by hand. See [claims-and-status.md](claims-and-status.md).

## How to read this archive

| Start here | What it is |
|---|---|
| [claims-and-status.md](claims-and-status.md) | **Central ledger.** Every claim with its status, scope and evidence. It governs if another file disagrees. |
| [notation-and-normalization.md](notation-and-normalization.md) | Scope tags [M]/[D]/[PI]/[ζ], zero conventions, the four Fourier conventions, grid and window units |
| [research-ledger.md](research-ledger.md) | Chronological record P0–P10, plus the two parallel conversations |
| [open-questions.md](open-questions.md) | The five most important open questions |
| [external-results.md](external-results.md) | Results by others relied on, and how each was checked |

## Lines of attack

| Line | Phase | Outcome | File |
|---|---|---|---|
| Proof by contradiction: baseline constraints | P0 | Admissible region nonempty; no contradiction | [approaches/01](approaches/01-contradiction-baseline.md) |
| Smoothed explicit formula + positivity of Λ | P1–P2 | Theorem K = Landau's limit; L4 withdrawn; Lemma Z open | [approaches/02](approaches/02-smoothed-explicit-formula.md) |
| Weil form split at height T | P3 | Almost positivity; threshold $e^{2a}\ge67$; DL open | [approaches/03](approaches/03-weil-form-height-split.md) |
| 2026 two-thirds results; resolution barrier | P4–P5 | Candidates A–F withdrawn as novelty; RES-1 to RES-4 | [approaches/04](approaches/04-two-thirds-paper-and-resolution-barrier.md) |
| Mollified moments hybrid | P6 | H1, H2 proved; needs a tiny-constant near-line density bound | [approaches/05](approaches/05-mollified-moments-hybrid.md) |
| **AC: inertia slack → near-line density** | P7–P9 | AC refuted at [M] and [D]; A″ proved; C sketched; AC_F open | [AC/](AC/README.md) |
| Spectral / ground state (parallel chat) | GS | Threshold λ* ≈ 1.151; circularity | [approaches/spectral-ground-state](approaches/spectral-ground-state.md) |
| Jensen polynomials / interlacing (parallel chat) | JEN | Reformulation only; propagation counterexample | [approaches/jensen-interlacing](approaches/jensen-interlacing.md) |

## Reproducibility

- [experiments/README.md](experiments/README.md) — every script with its invocation, the originally reported result, and the re-run result of 2026-10-19.
- [experiments/code/](experiments/code) — verbatim copies of the scripts. Checksums are in `experiments/code-sha256.txt`.
- [formalization/README.md](formalization/README.md) — the upstream Lean declarations used, with file:line. No Lean build was possible in this environment.

## Current state (2026-10-19)

- **Live line:** AC_F ([AC/AC-F-open-problem.md](AC/AC-F-open-problem.md)). It is not being worked on.
- **Recommended next action (not carried out).** Write out the interface Hilbert–Schmidt estimate and the trace-edge estimate for Theorem C, using the Lemma 1 decay and counting as in A″. This moves Theorem C from SKETCHED to PROVED, which makes the [D]-scope negative result solid before any work on the AC_F feasibility LP.

## Integrity notes

- Claims from earlier AI replies were **not** accepted on their authority. Each was re-checked, or else marked UNVERIFIED or SKETCHED.
- Withdrawn statements are kept verbatim where they first appear, and are labelled.
- Novelty: nothing here is claimed to be new. See [external-results.md](external-results.md).
