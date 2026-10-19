# 05 — Hybrid: pair correlation + mollified discrete moments of ζ′(ρ)

**Phase** P6 (2026-10-19 01:37 KST), main conversation. **Scope [D]/[ζ].**

## Idea

Make the Conrey–Ghosh–Gonek 19/27 argument unconditional, in the same way Alpöge–Furman made Montgomery's 2/3 unconditional. Write $u_\rho=\zeta'(\rho)B(\rho)$ with a mollifier $B$ of length $T^{1/2-}$. The two moments are
$$S_1=\sum\zeta'(\rho)B(\rho)\sim\tfrac{19}{24}NL,\qquad S_2=\sum\zeta'(\rho)B(\rho)\,\zeta'(1-\rho)B(1-\rho)\sim\tfrac{57}{64}NL^2 .$$
Under RH, Cauchy–Schwarz gives $N_s\ge S_1^2/S_2\to19/27$. According to Conrey–Ghosh–Gonek, RH is used only to read $S_2$ as $\sum|u_\rho|^2$.

## Results

| ID | Statement | Status |
|---|---|---|
| HYB-0 | Levinson's final bound (41.7%) is satisfied by the ceiling law and by its split version, so adding it changes nothing | PROVED (direct check) |
| HYB-1 | **H1.** In the free-value configuration model, the scalar data $(S_1,S_2)$ give no unconditional bound. One off-line pair $(x,y)=(w/2+z,\ w/2-z)$ contributes $(w,\ \lvert w\rvert^2/2-2\lvert z\rvert^2)$, which covers $\mathbb C\times(-\infty,\lvert w\rvert^2/2]$. | PROVED (re-checked in consolidation) |
| HYB-2 | **H2 (transfer lemma).** $N_s\ge\bigl(\lvert S_1\rvert-\sqrt{2pE}\bigr)_+^2/(S_2+E)$, with $E=\sum_{\text{off-line}}\lvert\zeta'B\rvert^2$. Thresholds with $p\le0.1638N$ (from the 2/3 theorem): to certify 0.6725 needs $E\le9.19\cdot10^{-4}NL^2$; 0.6818 needs $4.55\cdot10^{-4}$; 0.69 needs $1.80\cdot10^{-4}$; 0.70 needs $1.32\cdot10^{-5}$. | PROVED (lemma); thresholds are arithmetic (`hybrid-moments/hybrid.py`) |
| HYB-3 | A pair at normalized distance Δ has $\lvert\zeta'B\rvert^2\approx(4\pi\Delta)^2\times$ typical | UNVERIFIED heuristic |
| HYB-4 | H3: the inertia (matrix) version needs a "mollified pair correlation" with four $\zeta'B$ factors; judged beyond current technology except possibly for short mollifiers | UNVERIFIED assessment |

## Obstruction

Everything reduces to off-line zeros at normalized distance between about $10^{-3}$ and $1$:
- pair correlation cannot see them (RES-*);
- mollified moments cannot absorb them without a near-line density bound with very small constants.

## Literature status

- Conrey–Ghosh–Gonek (19/27 under RH and GLH): the text was read.
- Bui–Heath-Brown (GLH removal): **not read**, because the fetch was rate-limited.
- No follow-up of the 2/3 paper found in the search uses mollified moments of $\zeta'(\rho)$.
