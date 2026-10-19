# Spectral / ground-state rigidity for Weil's operator

**Source.** The separate claude.ai conversation "Ground-state rigidity and Riemann Hypothesis" (chat `de654dc8`, 2026-10-19 00:38 KST, same project). Content is transcribed from that conversation's final reply. **Only the small constants script was re-run here** ([../experiments/code/ground-state](../experiments/code/ground-state)). The other statements were **not re-audited** during this consolidation, so they carry the statuses below and no stronger ones.

## Idea

Turn Weil's quadratic form on $I=[-L,L]$ ($L=\log\lambda$) into a self-adjoint operator $A_\lambda$. Then use a Perron–Frobenius principle (positivity improvement) to get a simple, even ground state, and combine Connes–van Suijlekom's real-zeros theorem with Hurwitz's theorem to reach RH.

## Key equations (as reported)

**Archimedean part:**
$$\frac1{2\pi}\int\theta|\hat\varphi|^2=c_\infty\|\varphi\|^2+\tfrac12\iint w(u-v)|\varphi(u)-\varphi(v)|^2,$$
with $w(y)=e^{|y|/2}/(2\sinh|y|)$ and $c_\infty=\psi(\tfrac14)-\log\pi=-5.37218\ldots$.

**Operator:**
$$A_\lambda=c_\infty+\kappa+J_I-\sum_{n<\lambda^2}\frac{\Lambda(n)}{\sqrt n}(T_n+T_n^*)+2|C\rangle\langle C|-2|S\rangle\langle S|,$$
with $C=\cosh(u/2)$, $S=\sinh(u/2)$, and pole kernel $2\cosh\frac{u-v}2$ of signature $(1,1)$.

## Claims

| ID | Statement (as reported) | Status in this archive |
|---|---|---|
| GS-1 | Exact form of $A_\lambda$: self-adjoint via Kato, with compact resolvent | UNVERIFIED (not re-audited) |
| GS-2 | **Theorem A (sharp threshold).** Let $y_*=0.2811995743\ldots$ solve $2\cosh(y/2)=w(y)$, and $\lambda_*=e^{y_*/2}\approx1.1510$. (i) For $\lambda\le\lambda_*$, $e^{-tA_\lambda}$ is positivity improving, so the ground state is simple, positive and even. (ii) For $\lambda>\lambda_*$, positivity improvement fails for small $t$. (iii) The pole operator is the only defect. | SKETCHED (proof sketch in the source). $y_*$ and $c_\infty$ re-computed: see experiments. |
| GS-3 | **Theorem B (cluster collapse).** $\mu_k(\lambda)\le e^{-2\pi e^{-2\delta}\lambda^2}$ and $\lVert A_\lambda v_\lambda\rVert\le e^{-\pi e^{-2\delta}\lambda^2}\lVert v_\lambda\rVert$ for $v_\lambda=\chi_L\Phi$ | UNVERIFIED (not re-audited) |
| GS-4 | **Proposition C.** $\lvert\mu_1\rvert\le\lVert A_\lambda v\rVert/\lvert\langle v,\xi_\lambda\rangle\rvert$. Consequently any $L^2$-weighted overlap estimate of the needed strength implies RH, which makes that route circular. | Inequality PROVED (two-line argument, re-checked). The consequence is SKETCHED (depends on GS-3). |
| GS-5 | The chain (H1 simple even ground state) + (H2 transform convergence) + Connes–van Suijlekom + Hurwitz ⇒ RH is valid but gives no leverage | assessment |
| GS-6 | Overlap with a June 2026 Zenodo note and with Suzuki (arXiv:2606.09096) | UNVERIFIED literature claims |

## Obstruction

- Positivity improvement fails beyond $\lambda\approx1.151$ because of the pole term.
- The spectral gap collapses super-exponentially (GS-3), so perturbation estimates are useless.
- Transform convergence in any $L^2$-weighted form is already as strong as RH (GS-4).

## Suggested directions from the source (not pursued)

1. A cluster-level real-zeros theorem.
2. An even-sector-only theorem.
3. Eventual positivity (Daners–Glück–Kennedy).
4. Weak transform convergence via the regularized determinants of Connes–Consani–Moscovici.
