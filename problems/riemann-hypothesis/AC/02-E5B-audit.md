# E5B — adversarial audit of AC (phase P8, 2026-10-19 08:28 KST)

**Task given.** Audit AC skeptically: verify definitions, stress-test the spacing-1 lattice, look for repaired versions, and re-run independent numerics.

**Source.** The P8 reply in the main conversation. The experiments are E1–E5b in [experiments/code/ac-audit](../experiments/code/ac-audit). Later corrections from [E6](03-E6-audit.md) are marked ⟶.

## Findings as reported in E5B, with current status

| E5B finding | E5B status | Current status |
|---|---|---|
| AC is false as stated: the spacing-1 lattice has $Q^{\mathrm{pairs}}=2M_{\psi^2}\succeq0$ (Theorem A) | proved (periodic / infinite) | PROVED for infinite families ⟶ the finite-family version is A″ ([theorem-A-family](theorem-A-family.md)) |
| Finite grid: $\operatorname{tr}Q_-\le\zeta(3)B^2/(4\pi^4)$ uniformly in $d$ (Theorem A′) | proved | ⟶ constant **WITHDRAWN** (non-uniform in $L$), replaced by A″ |
| Density-one lattice: $\operatorname{tr}Q_-/\text{pair}\le e^{\pi\Delta}-1$ (Theorem B) | proved (infinite lattice) | PROVED in the periodic model; other versions SKETCHED |
| Closed form $\rho(s,\Delta)$ for indicator lattices | proved + cross-checked | PROVED (periodic model); continuum limit NUMERICALLY TESTED |
| Theorem C: Theorem S's data allow 25.6% / 29.4% / 30.8% of zeros in far pairs (indicator / MT / taper 0.1) | proved | ⟶ SKETCHED; scope [D] only ([theorem-C](theorem-C.md)) |
| Lemma B valid; the paper's Poisson lemma is for real γ only | audited | PROVED (bi-infinite); finite-grid edge leak documented |
| RT+ valid | audited | PROVED |
| Theorem S: the $(\lambda-2)^2$ slack is not trace-norm stable | correction | WITHDRAWN slack; $2\operatorname{tr}Q'_-$ term SKETCHED |
| Pair bound sharpened to $[(R-1)N-2p+m_2]/2$ | correction | SKETCHED (inherits S) |
| "$c\approx0.12$" was a finite-size artifact | withdrawal | WITHDRAWN |
| NL comparison with Selberg was misleading (Jutila) | withdrawal | WITHDRAWN |

## Key numbers (reported in E5B; re-run status in [experiments/README.md](../experiments/README.md))

**Exact lattice ratios** $\operatorname{tr}Q_-/\sum(S-1)$, indicator window, spacing 2 (zero density 1):

| Δ | 0.5 | 1 | 2 | 3 | 5 |
|---|---|---|---|---|---|
| ratio | 0.564 | 0.2545 | 0.0234 | 0.00152 | $4.7\cdot10^{-6}$ |

**Finite segments** at spacing 1, bi-infinite grid, indicator window. Ratio at segment length $L=8,\ 64,\ 512$:

| Δ | $L=8$ | $L=64$ | $L=512$ |
|---|---|---|---|
| 0.5 | 0.389 | 0.085 | 0.015 |
| 2 | 0.727 | 0.217 | 0.043 |

**Mixed configuration, taper window.** $\operatorname{tr}Q^{\mathrm{pairs}}_-$ is constant in $d$ ($2.154$ at $\Delta=0.5$; $36.54$ at $\Delta=1$) for $d=301$–$1201$. It is a pure interface effect.

**Adversarial search** (simulated annealing, density-constrained): weak. It never assembled long spacing-2 runs, whereas explicit clusters reach the lattice value. Search failure is not evidence of a lower bound.

## Admissibility analysis (E5B §3–4)

The missing hypothesis in AC was an admissibility class. Variants examined:

| Variant | Finding |
|---|---|
| Density ≤ 1 (pairs only) | Not refuted, but $c(\psi,\Delta_0)\le(e^{\pi\Delta_0}-1)/(S(\Delta_0)-1)$. |
| Local counting with bounded excess at scale $O(1)$ | Unknown for ζ, probably false: unconditional local-count variance grows like $(1/\pi^2)\log n$. |
| Known local counting $N(t,t+1)\ll\log t$ | Allows density-2 clusters of length up to about $\log T$, so AC still fails as $T\to\infty$. |
| Averaging over translations | Useless: the counterexamples are translation-invariant. |

## Literature found in E5B

- Jutila: $N(\sigma,T)\ll_cT\log T\cdot T^{-c(\sigma-1/2)}$ for every $c<1$. This was cited through arXiv:1404.3080, which attributes it to Jutila; Jutila's paper itself was not read. In normalized units this is decay $e^{-2\pi c\Delta}$, so even a valid NL from this route would be weaker.
- Fujii's unconditional CLT for local zero counts, cited through arXiv:1404.3080.
