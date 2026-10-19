# 03 — Weil's quadratic form split at a height T (Guinand–Weil, Connes–Consani supports)

**Phase** P3 (2026-10-19 00:28 KST), main conversation. **Normalization:** [notation §6](../notation-and-normalization.md). **Scope [ζ]** (relative to external numerics).

## Idea

Write Weil's form exactly. Split the zero sum at the height to which RH has been verified, bound the tail, and see what positivity says about a hypothetical zero at height $t_0$, using localized test functions $f=f_0(u)\cos(t_0u+\varphi)$.

## Results

| ID | Statement | Status |
|---|---|---|
| WEIL-1 | The normalization of the Guinand–Weil identity was checked numerically with the first 415 zeros (height ≤ 700). Residual $5.5\cdot10^{-16}$ at $a=\tfrac12\log2$, where $P\equiv0$; about $4\cdot10^{-9}$ after grid refinement at $a=1.2$ and $1.6$. | NUMERICALLY TESTED (identity: EXT) |
| WEIL-2 | $S_{\mathrm{low}}(T)=\sum_{\lvert\operatorname{Re}\gamma\rvert\le T}h(\gamma)\ge0$ for $T\le3\cdot10^{12}$ | PROVED rel. EXT-PT |
| WEIL-3 | $\lvert S_{\mathrm{high}}(T)\rvert\le\frac2\pi e^a\lVert g''\rVert_1(\log T+1)/T$ for $T\ge10$. Uses Trudgian's $N(T)$ bound to get $N(t)\le\frac t{2\pi}\log t$; the margin was checked numerically on $[10,10^{16}]$ (minimum 0.62), and is asymptotically clear beyond. | PROVED rel. EXT-TR |
| WEIL-AP | **Almost positivity.** $W(f*f^*)\ge-1.2618\cdot10^{-11}\,a\,e^a\lVert f'\rVert_2^2$ for every real $f\in C^2_c([-a,a])$ | PROVED rel. EXT-PT, EXT-TR (re-checked in consolidation) |
| WEIL-Q | Quadruple contribution $C^2-S^2+O(t_0^{-2})$, with $C=\int f_e\cosh\delta_0u$ and $S=\int f_o\sinh\delta_0u$ | SKETCHED |
| WEIL-ARCH | $A(g)\ge g(0)[\log(t_0/2\pi)-10^{-20}]-O(\lVert f_0\rVert\lVert f_0'\rVert/t_0)$ | SKETCHED (constants not re-derived) |
| WEIL-P | $P(g)\le2\lambda_{\max}(a)\,g(0)\le2S(e^{2a})\,g(0)$, where $S(X)=\sum_{n\le X}\Lambda(n)/\sqrt n$. **Caveat found in consolidation:** the P3 report wrote $\lvert P\rvert\le2\lambda_{\max}g(0)$. The absolute value would need $\lvert\lambda_{\min}\rvert\le\lambda_{\max}$, which was not shown. Only the one-sided bound is used and proved. | PROVED (one-sided); two-sided UNVERIFIED |
| WEIL-λ | $\lambda_{\max}(a)\ge\log2/(2\sqrt2)=0.2451$ for every $a>\tfrac12\log2$: a jump as soon as $n=2$ enters | PROVED |
| WEIL-THR | At $t_0=3\cdot10^{12}$ the target $\tfrac12\log(t_0/2\pi)=13.4459$ needs $e^{2a}\ge67$, since $S(66)=13.3355<13.4459<S(67)=13.8492$ (30-digit computation) | PROVED (finite computation) |
| WEIL-COMB | $W\ge g(0)[\log(t_0/2\pi)-2\lambda_{\max}(a)]-R$. So localized positivity is automatic, and carries no information, unless $\lambda_{\max}(a)>\tfrac12\log(t_0/2\pi)$. | SKETCHED (inherits WEIL-Q and WEIL-ARCH) |
| WEIL-λnum | $\lambda_{\max}(a)\approx0.55e^a$; threshold $e^{2a^*}\approx580$ at $3\cdot10^{12}$ | NUMERICALLY TESTED (`prime-threshold/`) |
| WEIL-CC | Dictionary with Connes–Consani: their support $[2^{-1/2},2^{1/2}]$ is our $a=\tfrac12\log2$, where $P\equiv0$; their $\tilde f(0)=\tilde f(1)=0$ is our Pole $=0$. Their "vanishing at 0" condition could not be translated. | supports and poles VERIFIED; vanishing condition UNVERIFIED |
| WEIL-DL | **Detection lemma.** An off-line zero at $t_0$ forces $W<0$ for some $f$ with $a\le C_0\log t_0$, under local separation | **OPEN** |

## Obstruction

The prime sum $P(g)$ becomes competitive only when $e^{2a}$ grows like $(\log t_0)^2$. In that regime no positivity theorem is known, and full positivity over all supports *is* Weil's criterion (RH-equivalent).

## Strongest surviving result

Almost positivity (WEIL-AP) and the automatic-positivity threshold (WEIL-THR). Both are elementary consequences of known results; no novelty is claimed.

## Literature

- Connes–Consani (Selecta 2021, arXiv:2006.13771): archimedean-place positivity with no primes.
- Trudgian (2014): explicit $S(T)$.
- Platt–Trudgian (2021).
