# Formalization audit (Lean)

## What this project formalized

**Nothing.** No Lean code was written in this project. Every claim in this archive labelled PROVED is a paper-level proof, re-checked by hand. No claim here is FORMALLY VERIFIED.

## What exists upstream and was used

The upstream Lean formalization is the Alpöge–Furman paper's companion repository:

| Field | Value |
|---|---|
| Repository | `anthropics/formal-math`, subdirectory `zeta23` |
| Commit | `e1a4e6508154ea59f030480661590a9fe3018011` (2026-10-05) |
| Toolchain | `leanprover/lean4:v4.33.0-rc2`; Mathlib `51e6992efd06126df61a496bebf8f49482a4e129` |
| Upstream build command | `lake build` (the README also lists `lake build Solution.XiPrime` and `lake env lean scripts/PrintAxioms.lean`) |
| **Build in this project** | **Not run.** `elan`, `lean` and `lake` are not installed in the workspace, and a Mathlib build was not attempted. Everything below comes from **reading the source**. |

In the main conversation (P5, P9) the repository was cloned to a session scratch directory and read. The clone is not part of this archive. Line numbers below were re-checked against that clone on 2026-10-19 during consolidation.

## Declarations relied on

| Declaration | File:line | What it states (as read) | Used for |
|---|---|---|---|
| `paperFT` | `Zeta23/Defs.lean:44` | $\int f(u)e^{izu}du$ | normalization (notation §2) |
| `gammaOf` | `Zeta23/Defs.lean:105` | $(\rho-\tfrac12)/i$, complex for off-line ρ | Δ enters the vectors (E6 B2) |
| `ZeroConfig` | `Zeta23/Defs.lean:120` | abstract zero multiset with reflection and multiplicity | scope tag [D] |
| `Gz`, `Az`, `Ez` | `Zeta23/Defs.lean:304, 311, 315` | full, $I'$-restricted and remainder Gram matrices | E6 A |
| `blockA` | `Zeta23/ZeroSide.lean:316` | $\sum_z m_z\,v_zv_z^{\mathsf T}$ (`vecMulVec`, transpose) | transpose Gram (E6 B4) |
| `blockP`, `blockQ` | `Zeta23/ZeroSide.lean:460, 463` | $c^{-1}\cdot$onPart and $c^{-1}(\text{blockA}-\text{onPart})$ | P/Q split |
| `blockP_add_blockQ` | `Zeta23/ZeroSide.lean:466` | $P+Q=c^{-1}\,\text{blockA}$ | — |
| `rtrace_blockP_le` | `Zeta23/ZeroSide.lean:513` | trace bound on the P block | — |
| `blockInputs` | `Zeta23/ZeroSide/Final.lean:57` | `BlockInputs` holds for **every** `ZeroConfig` (given valid parameters) | Theorem C, row "BlockInputs" |
| `ExplicitFormulaPaper` | `Zeta23/Hypotheses.lean:48` | H-EF | scope tag [PI] |
| `RiemannVonMangoldt` | `Zeta23/Hypotheses.lean:67` | H-RvM (main count + local count) | Theorem C, AC_F |
| `PaperInputs` | `Zeta23/Hypotheses.lean:147` | bundle EF, RvM, cheb, MV, Gamma | scope tag [PI] |
| `BlockInputs`, `TailInputs` | `Zeta23/Assembly/Inputs.lean:42, 57` | assembly interfaces | Theorem C, Theorem S |
| `eventually_tailInputs` | `Zeta23/Tail.lean:651` | `TailInputs` eventually, from the **local count** plus window facts | Theorem C, row "TailInputs" |
| `hasSum_phiHatR_mul`, `hasSum_phiHatR_sq` | `Zeta23/Poisson.lean:347, 367` (re-exported at 388, 394) | Poisson identities for **real** γ only | AC-B (Lemma B for complex Δ is ours, paper-level) |
| `half_le_a` | `Zeta23/Taper/Params.lean:95` | $a\ge\tfrac12$ | uniform constant in A″ Lemma 1 |
| `rank_trace_ineq` | `Zeta23/LinAlg/RankTrace.lean:163` | for $P\succeq0$, $Q$ Hermitian, $\operatorname{rank}P\le r$, $\operatorname{posIndex}Q\le b$, $c>0$: $c\operatorname{tr}P-\tfrac{c^2}4r+2c\operatorname{tr}Q-c^2b\le\|P+Q\|_F^2$ | RT+ is the $c=2$ case with the slack kept (`rank_trace_ineq_two` at :260) |
| `lemmaR_tight` | `Zeta23/ZeroSide/TightMult.lean:93` | rank–trace certificate is tight given only those quantities | context for RT+ |
| `ceiling_stability` | `Zeta23/PairCeiling/Stability.lean:305` | stability inequality for bandwidth-one certificates | RES-2, RES-3 |
| `ceiling_law256` | `Zeta23/PairCeiling/CeilingLaw256.lean:38` | ceiling $0.6818287+\dots$, **hypothesis `EnclOK`** | RES-2, RES-3 |
| `PaperInputs.of_literature`, `.of_three` | `Zeta23/Final.lean:50, 133` | build `PaperInputs` from literature-form EF, RvM, MV, Γ-facts | scope note below |
| `thmB₀_mult` | `Zeta23/FinalMult.lean:350` | $\forall\varepsilon>0\ \exists T_0\ \forall T\ge T_0:\ (2/3-\varepsilon)N(T,2T)\le N_0^s(T,2T)$ for Mathlib's `riemannZeta` | the 2/3 theorem itself |
| `two_thirds_simple_on_critical_line` | `Challenge.lean:142` (statement, proof `sorry` **by design**: this is the trusted challenge side); `Solution.lean:60` (proof `:= Zeta23.thmB₀_mult`) | same statement | — |

## What the upstream claims, and what we checked

- **Upstream claim** (README): the formalization is `sorry`-free and the headline theorems have **no hypotheses**. `#print axioms` reports only `propext`, `Classical.choice` and `Quot.sound`. `Challenge.lean` and `Solution.lean` are matched by `leanprover/comparator`.
- **What we checked by reading:**
  - `Challenge.lean` contains deliberate `sorry`s (the statement side).
  - `Challenge/XiPrime.lean` also has `sorry`s, for the same reason.
  - A `grep` for `sorry` in `Zeta23/` finds only comments.
  - The only `axiom` declarations are in a tactic test file (`FromPNTPlus/Tactic/AdditiveCombination.lean:183–184`, inside an `example`). The `scripts/PrintAxioms.lean` audit was **not run**.
- **Not checked:** that the project builds, that comparator passes, or that the axiom audit output is as claimed. These need a Lean toolchain and a Mathlib build.

## Formal vs paper-level in this archive

| Claim in this archive | Formal counterpart | Status here |
|---|---|---|
| RT+ (with slack) | `rank_trace_ineq` covers the slack-free part only | PROVED (paper-level). The slack terms are **not** formalized. |
| Lemma B for complex $\zeta$ | none (`Poisson.lean` covers real γ only) | PROVED (paper-level) |
| Theorems A, A″, B, C, S | none | paper-level only |
| BlockInputs / TailInputs for Theorem C's configuration | `blockInputs`, `eventually_tailInputs` apply to every `ZeroConfig` satisfying their hypotheses | the formal theorems exist; that our configuration meets their hypotheses (local count, valid params) is checked on paper |
| AC, AC_F, NL, RH | none | **not formally verified**, and no formal statement exists |

## Scope note: what is [PI]

Upstream builds `PaperInputs zetaZeroConfig` from the literature-form explicit formula, RvM, MV and Γ-facts. According to its README, the analytic inputs themselves are also proved in Lean. So the actual zeros satisfy `PaperInputs`, per the unbuilt upstream.

Theorem C's configurations violate H-EF, so they are **not** [PI].

## Next verification step

Install elan with the pinned toolchain and run, in `zeta23/`:
```
lake exe cache get
lake build
lake env lean scripts/PrintAxioms.lean
```
Record the output. This confirms the upstream claims; it does not verify anything in this archive.

Formalizing Theorem A″ in Lean, on top of `blockA`, would be the first claim of this project to become FORMALLY VERIFIED.
