# Experiments

All numerical work of the project is listed here. **Numerics are evidence, never proof.** The "Can establish" column says what each run can and cannot support.

## Provenance and reproduction

- **Scripts.** `code/<experiment>/` holds verbatim copies of the scripts as run in the original sessions. Checksums are in [code-sha256.txt](code-sha256.txt).
  - `jensen-interlacing/` and `ground-state/` were **recovered from conversation transcripts** (their headers say so). The original session's files and outputs for those two were not preserved.
  - `jensen-interlacing/ce_exact.py` merges three inline sympy checks into one file. The code lines are verbatim; only the print labels were added.
- **Original outputs.** Mostly these were *not* saved as files: the original numbers survive only as quoted in the conversation replies, and the "Original reported" column quotes them. Two partial output files survived: [outputs/original-session/](outputs/original-session). Both original runs hit a timeout.
- **Re-run of 2026-10-19.** Outputs are in [outputs/rerun-2026-10-19/](outputs/rerun-2026-10-19), with exit codes and wall-clock seconds in `log-A.tsv`, `log-B.tsv` and `log-C.tsv`.
  - Environment: Python 3.13.16, numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0, sympy 1.14.0; 2 CPUs, 8 GB memory cap; `OPENBLAS_NUM_THREADS=1`.
  - The three lanes ran **concurrently**, so runtimes are inflated and memory was shared.
- **How to re-run** (from the repository root):
  ```
  OPENBLAS_NUM_THREADS=1 sh problems/riemann-hypothesis/experiments/rerun.sh A OUTDIR   # lanes A, B, C
  ```
  [rerun.sh](rerun.sh) copies each code directory to a temporary directory, so side files (`zeros.pkl`, `a.pkl`) never touch `code/`. It runs `timeout T python3 script [args]`. No random seeds were changed: scripts that use RNGs seed them internally.

## Results

"Match" means the re-run reproduces the numbers quoted in the original reply, to the printed precision.

### Lane A — explicit formula, Weil, resolution, hybrid, ground state, AC round 5

| Experiment | Script | Purpose | Original reported | Re-run (exit, s) | Match | Can establish / cannot |
|---|---|---|---|---|---|---|
| weil-identity | `zeros.py` | first zeta zeros to height 700 via `mpmath.zetazero` | 415 zeros | 0, 108: `415 700.2967…` | yes. The regenerated `zeros.pkl` is **identical** to the archived one (415 values, max difference 0.0). | input data only |
| weil-identity | `weil.py` | Guinand–Weil identity, zeros vs. right side | residual $5.5\cdot10^{-16}$ at $a=\tfrac12\log2$ | 0, 24: $-5.52\cdot10^{-16}$; $2.8\cdot10^{-8}$, $5.4\cdot10^{-8}$ at $a=1.2, 1.6$ (coarse grid) | yes | normalization check (WEIL-1). It cannot verify RH or anything beyond height 700. |
| weil-identity | `weil2.py` | grid refinement of the same | ≈ $4\cdot10^{-9}$ after refinement | 0, 52: $1.05\cdot10^{-7}$ → $3.83\cdot10^{-9}$ (12001 points) | yes | as above |
| weil-identity | `checks.py` | Trudgian margin; $S(66)$, $S(67)$; tail constant; $c_\infty$ | margin 0.62; $S(66)=13.3355<13.4459<S(67)=13.8492$; $1.2618\cdot10^{-11}$ | 0, 0: 0.62187; 13.33548…, 13.44588…, 13.84917…; $1.26176\cdot10^{-11}$; $c_\infty=-5.372183…$ | yes | WEIL-THR is an exact finite computation (30 digits). The margin check covers $[10,10^{16}]$ on a grid only. |
| prime-threshold | `thresh.py` | $\lambda_{\max}(a)$ of the prime form | $\lambda_{\max}\approx0.55e^a$ | 0, 4: e.g. $\lambda_{\max}(3)=11.27$ | yes | discretized eigenvalue, not certified (WEIL-λnum) |
| prime-threshold | `thresh2.py` | bisection for $\lambda_{\max}(a^*)=13.446$ | $e^{2a^*}\approx580$ | 0, 111: 579.2 ($M=1500$), 580.4 ($M=3000$) | yes | as above |
| landau-lp | `lp.py` | LP for Landau's constant $V$, cosine polynomials of degree ≤ 48 | $V\approx34.49$ | 0, 103: κ = 0.057986, so $V=2/\kappa\approx34.49$ | yes | upper estimate on a grid, agreeing with the published bracket (EF-V); not a certified bound |
| resolution-barrier | `resolution.py` | deformation identity RES-1 on a 256-periodic toy law | agreement $5\cdot10^{-15}$; change $\asymp\Delta^2$ | 0, 0: max error ≤ $5.3\cdot10^{-15}$; $\sum\lvert s_\Delta-s_0\rvert/\Delta^2\to7.733$ | yes | checks the algebraic identity; the barrier itself (RES-2/3) rests on `EnclOK` |
| hybrid-moments | `hybrid.py` | thresholds of the transfer lemma H2 | $9.19\cdot10^{-4}$, $4.55\cdot10^{-4}$, $1.80\cdot10^{-4}$, $1.32\cdot10^{-5}$ | 0, 0: $9.193\cdot10^{-4}$, $4.546\cdot10^{-4}$, $1.795\cdot10^{-4}$, $1.321\cdot10^{-5}$ | yes | arithmetic only |
| ground-state | `constants.py` | $y_*$ and $c_\infty$ | $y_*=0.2811995743$; $c_\infty=-5.37218$ | 0, 0: $y_*=0.28119957432…$; $c_\infty=-5.37218341922…$ | yes | constants only; GS-2's theorem is not tested |
| ac-round5-slack | `slack.py` | Lemma B: pair block eigenvalues $\{1+S,1-S\}$ (periodic model) | matches prediction | 0, 1: matches to 6 digits for Δ ≤ 1 | yes | AC-B in the periodic model |
| ac-round5-slack | `slack2.py` | random pair configurations: $\operatorname{tr}Q_-/\sum(S-1)$ | "≥ 0.40" | 0, 5: minimum over the ranges is **0.395** ($p=100$, $\Delta_{\max}=0.2$) | **rounding**: P7's "≥ 0.40" rounds 0.395 up | random sampling. It says nothing about worst cases (AC was later refuted). |
| ac-round5-slack | `slack4.py` | regular arrays, spacing 0.5–3 | full cancellation at spacing 1 | 0, 37: ratio 0.000 at $s=1$ for all Δ | yes | consistent with Theorem A |
| ac-round5-slack | `slack5.py` | regular arrays at spacing ≥ 2 | 0.30, 0.12, 0.15 at Δ = 1, 2, 3 ($s\approx2$) | 0, 9: 0.300, 0.122, 0.146 | yes | these values are the **withdrawn** "c ≈ 0.12" (finite-size artifact; see AC-c012) |
| ac-round5-slack | `slack3.py` | Nelder–Mead adversary, $d=61$ | ≥ 0.34 | 0, 687: minimum combined-slack ratio 0.3438 ($p=15$, Δ = 0.6) | yes | a local search is not a lower bound. The minimizers have pair gaps below 1, which the later work treats as the regime that refutes AC. |
| ac-round5-slack | `slack6.py` | local search from arrays, $d=121$ | did not go lower | 0, 440: Δ = 1: 0.3434 (start 0.3420), 0.5766 (0.5801); Δ = 2: 0.2225 (0.2093), 0.3043 (0.3024) | yes: nothing lower than the lattice starts. The printed "minimum" sometimes exceeds the start, because the start is a jittered configuration evaluated separately. | as above |

### Lane B — AC audit (E1–E6)

| Experiment | Script | Purpose | Original reported | Re-run (exit, s) | Match | Can establish / cannot |
|---|---|---|---|---|---|---|
| E1 | `e1_singlepair.py` | single pair: bi-infinite spectrum vs Lemma B; finite-grid I1 | I2 matches $\{1\pm S\}$; I1 values aliased | 0, 4: I2 matches for 4 windows × 3 Δ | yes | I2 checks AC-B. **I1 columns reproduce the old quadrature aliasing by design**; they are superseded by E1b. |
| E1 | `e1b.py` | I1 with exact sinc: $\sum v^2\to1$, $\sum\lvert v\rvert^2\to S$ | convergence | 0, 3: e.g. Δ = 1: 0.99999 and 42.6129 at grid ±10⁶ | yes | finite-grid edge leak decays as the grid grows |
| E2a | `e2_lattice.py` | infinite lattices: periodic vs fiber vs closed form | three methods agree; ratio 0 at $s=1$ | 0, 40: agree to $\le2\cdot10^{-4}$; ratio $-0.00000$ at $s=1$ for every window | yes | Theorem A numerically; closed form AC-ρ |
| E2b | `e2b.py` | exact lattice ratio at $s=2$ vs Theorem B bound | indicator: 0.564, 0.2545, 0.0234, 0.00152, $4.7\cdot10^{-6}$ (Δ = 0.5, 1, 2, 3, 5) | 0, 16: 0.5640, 0.2545, 0.02338, 0.001521, $4.734\cdot10^{-6}$ | yes | AC-B2's bound holds in every row; periodic model |
| E3 | `e3_segments.py` | finite spacing-1 segments, bi-infinite grid | Δ = 0.5: 0.389, 0.085, 0.015; Δ = 2: 0.727, 0.217, 0.043 ($L=8$, 64, 512) | **137 (killed for out-of-memory), 1285.** Partial output: 6 indicator rows. The 4 rows in the original partial output are identical; 2 new rows ($s=1.5$). Spacing-1 values: Δ = 0.5: 0.3891, 0.0847, 0.0151; Δ = 2: 0.7267, 0.2174, 0.0434 | yes, on the overlap. The taper rows were never produced, in either the original run or the re-run. | consistent with A″'s decay; not a proof |
| E4 | `e4_mixed.py` | mixed configurations: $\operatorname{tr}Q_-$ is constant in $d$ | taper: 2.154 (Δ = 0.5), 36.54 (Δ = 1) for $d=301$–1201 | 0, 27: 2.154–2.155; 36.528–36.543 | yes | interface effect, [M] |
| E4b | `e4b.py` | bulk HS/N extrapolation | admissible fractions | 0, 26: indicator admissible at 0.20, not at 0.24; taper admissible to 0.28 | yes | brackets the E4c thresholds |
| E4c | `e4c_exact.py` | exact bulk thresholds for Theorem C | 0.2561, 0.2944, 0.3075 | 0, 16: 0.2561, 0.2944, 0.3075 | yes | bulk only (AC-C-thr); the interface terms are what keeps C SKETCHED |
| E5b | `e5b.py` | explicit density-one clusters → lattice value | 0.3366 … 0.2633 → 0.2545 (indicator, Δ = 1) | 0, 4: identical | yes | AC-B2, NUMERICALLY TESTED |
| E5 | `e5_adv.py 2` | simulated-annealing adversary | weak; partial output (timeout) | 0, 69: the first 6 lines identical to the original partial output, plus 2 more lines | yes (on the overlap) | search failure is not a lower bound |
| E6 | `e6_check.py` | A″ sanity check: finite grid 300, ℓ = 100 | table in [theorem-A-family](../AC/theorem-A-family.md) | **137 (killed by out-of-memory), 274.** The two indicator rows were printed first: 13.9293 / 15.8390 / 122.24 / 267.61 and 338.9501 / 389.4513 / 2188.91 / 4161.29 | Indicator rows: yes. **Taper row: reproduction failure.** A solo re-run (`ac-audit--e6_check.solo.out`, `log-B-solo.tsv`) was also killed for out-of-memory (exit 137, 63 s) at the taper step, under the 8 GB cap. The script was not modified. | consistency with A″ only |

### Lane C — Jensen (recovered scripts)

| Experiment | Script | Purpose | Original reported | Re-run (exit, s) | Match | Can establish / cannot |
|---|---|---|---|---|---|---|
| jensen | `coeffs.py` | Taylor coefficients of Ξ at 80 digits → `a.pkl` | (output not preserved) | 0, 156 | n/a | input data |
| jensen | `test.py` | hyperbolicity of $J_{d,n}$ for $2\le d\le14$, $0\le n\le25$ | 338 cases hyperbolic, simple zeros | 0, 209: "cases: 338 non-hyperbolic: [] interlacing fails: []", for both the Jensen and the raw normalization | yes | JEN-6 for these 338 cases at 80 digits (floating roots with tolerance $10^{-30}$; not interval-certified). Says nothing about other (d, n). |
| jensen | `ce.py` | first float search (mpmath `polyroots`) | (superseded in the source by exact counts) | **1, 4: `NoConvergence`** in `polyroots` | **reproduction failure** | none. Superseded by `ce_exact.py`. |
| jensen | `ce2.py` | Sturm count via sympy `count_roots` | (as transcribed) | 0, 1: "d= 4 non-hyperbolic at n in [0..7]" | see note | `count_roots` counts **distinct** real roots (checked: $(x+4)^2(x+1)$ gives 2). The flag at $d=4$ is the double root, not a complex pair. |
| jensen | `ce_exact.py` | exact root counts with multiplicity (`real_roots`); $J_{4,0}$ roots | first failure $d=6$, $n=0$ | 0, 3: failures only at $n=0$ for $d=6..11$; $J_{4,0}$ has roots $-4,-4,-1.567,-1.049$ | yes | JEN-4 for $d\le11$, $n<40$ (exact). Reveals the multiplicity caveat recorded in JEN-4. |
