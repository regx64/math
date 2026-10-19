# AC as originally proposed (phase P7, 2026-10-19 ≈01:46 KST)

**Source.** The "continue" reply of the main research conversation, transcribed here. The transcription is faithful to the conversation text, but the normalization in phase P7 was a periodic toy model and was only later matched to the paper (see [03-E6-audit.md](03-E6-audit.md)). Treat the P7 normalization as **provisional**.

**Status of everything on this page:** superseded. Current statuses are in [claims-and-status.md](../claims-and-status.md) and summarized at the end of this page.

## Motivation

The rank–trace inequality of Alpöge–Furman (arXiv:2608.13637, Lemma 3.2; Lean `rank_trace_ineq` with $c=2$) discards nonnegative slack terms. The idea was to keep that slack: off-line pairs far from the line contribute large negative eigenvalues, and those should be paid for by the HS budget, which would give a near-line zero-density estimate.

## Model used in P7

- Bandwidth-one Gram vectors $v_z(k)=\hat\psi(z-k)$ with ψ even, supported in $[-\tfrac12,\tfrac12]$, and $\int\psi^2=1$.
- Numerics used the periodic Dirichlet model $v_z(k)=\frac1d\sum_{|j|\le(d-1)/2}e^{2\pi ij(z-k)/d}$, i.e. the indicator window.

## Statements as made in P7

**Lemma B.** $\sum_kv_z(k)^2=\int\psi^2$ for every complex $z$ (Poisson). A pair at normalized distance Δ gives a block with eigenvalues $1+S_\psi(\Delta)$ and $-(S_\psi(\Delta)-1)$, where
$$S_\psi(\Delta)=\frac{\int\psi^2\cosh(4\pi\Delta u)\,du}{\int\psi^2}\qquad\Bigl(\text{indicator: }\frac{\sinh2\pi\Delta}{2\pi\Delta}\Bigr).$$

**RT+.**
$$r\ge2\operatorname{tr}P+4\operatorname{tr}Q-4b-\|P+Q\|^2+2\operatorname{tr}Q_-+\sum_{q>0}(q-2)^2 .$$

**Theorem S (as stated in P7).**
$$2\operatorname{tr}(Q'_-)+\sum_{\lambda>0}(\lambda-2)^2\le(R(\psi)-1)N-2p-m_2+o(N),$$
and hence $\operatorname{tr}(Q^{\mathrm{pairs}}_-)\le(R-1)N-2p+o(N)$.

**AC conjecture (as stated in P7).** For each window ψ and each $\Delta_0$ there is $c=c(\psi,\Delta_0)>0$ such that, *for every finite family of pairs* with $\Delta_k\le\Delta_0$,
$$\operatorname{tr}(Q^{\mathrm{pairs}}_-)\ \ge\ c\sum_k\bigl(S_\psi(\Delta_k)-1\bigr).$$

**Theorem NL (conditional on AC, as stated in P7).**
$$\#\{\text{pairs}:\Delta_1\le\Delta\le\Delta_0\}\le\frac{(R-1)N}{c\,(S_\psi(\Delta_1)-1)}+o(N).$$
With $c=0.12$ and the indicator window, this was tabulated as $0.067N$ ($\Delta_1=1$), $0.0042N$ (1.5), $2.4\cdot10^{-4}N$ (2), and $6.8\cdot10^{-7}N$ (3). It was described as decay $e^{-2\pi\Delta}$ "vs Selberg $e^{-\pi\Delta/2}$".

**Numerical evidence quoted in P7.** Indicator window, scripts in [experiments/code/ac-round5-slack](../experiments/code/ac-round5-slack):

| Test | Reported ratio |
|---|---|
| Random positions | $\ge0.40$ |
| Nelder–Mead adversary ($d=61$) | $\ge0.34$ |
| Regular arrays at spacing ≈ 2, $\Delta=1,2,3$ | $0.30,\ 0.12,\ 0.15$ |
| Local search started from those arrays | did not go lower |

P7 noted that full cancellation occurs at spacing 1, and dismissed it as "twice the true zero density".

## What happened to each statement

| Statement | Current status | Where |
|---|---|---|
| Lemma B | PROVED on the bi-infinite grid. The finite grid has edge leak. | [03-E6-audit.md](03-E6-audit.md), claim AC-B |
| RT+ | PROVED | [theorem-S-and-NL.md](theorem-S-and-NL.md) |
| Theorem S, $(\lambda-2)^2$ slack | WITHDRAWN: not stable under the paper's trace-norm tail | [theorem-S-and-NL.md](theorem-S-and-NL.md) |
| Theorem S, $2\operatorname{tr}Q'_-$ term | SKETCHED | [theorem-S-and-NL.md](theorem-S-and-NL.md) |
| AC, unrestricted | **REFUTED** for [M] and [D] | [theorem-A-family.md](theorem-A-family.md), [theorem-C.md](theorem-C.md) |
| "c ≈ 0.12" | **WITHDRAWN**: finite-size artifact (one Fourier class of size 3). The exact lattice gives 0.0015 at Δ = 3. | [02-E5B-audit.md](02-E5B-audit.md) |
| Dismissal of the spacing-1 cancellation | **WITHDRAWN**: local clusters are allowed by the known constraints | [02-E5B-audit.md](02-E5B-audit.md) |
| Theorem NL | **WITHDRAWN**: its premise is refuted, and Theorem C shows it cannot follow from Theorem S's data | [theorem-S-and-NL.md](theorem-S-and-NL.md) |
| "Better than Selberg" | **WITHDRAWN**: Jutila already gives $e^{-2\pi c\Delta}$ for every $c<1$ | [../external-results.md](../external-results.md) |
