# Theorems A, A′, A″ — negative mass of off-line pair clusters (canonical)

Normalization: [notation §3–4](../notation-and-normalization.md). Throughout:
- $\psi$ is real, even, bounded and supported in $[-\tfrac12,\tfrac12]$, with $\int\psi^2=1$.
- $v_\zeta(k)=\int\psi(\xi)e^{2\pi i\xi(\zeta-k)}d\xi$ for $k\in\mathbb Z$ and $\zeta\in\mathbb C$.
- A pair at $m$ is $\{m-i\Delta,\ m+i\Delta\}$.
- For a family $F$ of points, $\mathbb G_F(k,l)=\sum_{z\in F}v_z(k)v_z(l)$, a transpose-Gram on $\mathbb Z\times\mathbb Z$.

**Scope: [M]** (arbitrary families). Nothing here uses arithmetic.

History: Theorem A and A′ were stated in [02-E5B-audit.md](02-E5B-audit.md). A′'s constant was found non-uniform in [03-E6-audit.md](03-E6-audit.md), which replaced it by A″. A″ was re-derived step by step for this archive (2026-10-19).

## Lemma 0 (compression is exact) — PROVED

The paper's hat-unit pair matrix is a principal submatrix of the bi-infinite matrix of the same family: $Q=P_\Gamma\,\mathbb G_F\,P_\Gamma$, where $\Gamma=\{0,\dots,d-1\}$ and $F$ is the set of pairs in $Z(I')$. This holds because every entry depends only on $(k,l)$ and $F$.

## Lemma 1 (decay of a single vector) — PROVED

Let $g(\xi)=\psi(\xi)e^{2\pi\xi\Delta}$ and $\hat g(s)=\int g(\xi)e^{2\pi i\xi s}d\xi$, so that $|v_{m-i\Delta}(k)|=|\hat g(m-k)|$.

- **Symmetry.** $g$ is real, so $|\hat g(-s)|=|\hat g(s)|$. Since ψ is even, $v_{\bar z}=\overline{v_z}$, so both members of a pair have the same moduli.
- **Indicator.** $\hat g(s)=\sinh(\pi(\Delta+is))/(\pi(\Delta+is))$. For integer $s\ne0$, $|\hat g(s)|\le\sinh(\pi\Delta)/(\pi|s|)$.
- **Paper's window $\psi_L$.** Here $g(\pm\tfrac12)=0$, so one integration by parts gives $|\hat g(s)|\le\|g'\|_1/(2\pi|s|)$, with
$$\|g'\|_1\le e^{\pi\Delta}\bigl(\|\psi'\|_1+2\pi\Delta\|\psi\|_1\bigr).$$
  $\psi_L$ is monotone on each half, so $\|\psi_L'\|_1=2/\sqrt a$, and $\|\psi_L\|_1\le1/\sqrt a$. With $a\ge\tfrac12$ (Lean `half_le_a`) this gives, **uniformly in L**,
$$|\hat g(s)|\le\frac{c}{|s|},\qquad c=\frac{e^{\pi\Delta}(2+2\pi\Delta)\sqrt2}{2\pi}.$$
- **Norm.** $\sum_{k\in\mathbb Z}|v_{m-i\Delta}(k)|^2=S_\psi(\Delta)$, by Plancherel.

*Re-audit note:* E6 stated $c=\cosh(\pi\Delta)/\pi$ for the indicator. That is valid but loose; $\sinh(\pi\Delta)/\pi$ suffices.

## Theorem A (infinite lattice is PSD) — PROVED, [M], infinite families

For any offset $x_0$, the bi-infinite matrix of the lattice $\{m+x_0\mp i\Delta:m\in\mathbb Z\}$ is
$$\mathbb G_\infty(k,l)=2\int\psi^2(\xi)\,e^{-2\pi i\xi(k-l)}\,d\xi,$$
a Toeplitz matrix with nonnegative symbol $2\psi^2$. It is therefore PSD (every finite principal submatrix is PSD) and **independent of Δ**.

*Proof.*
1. Fix $k,l$ and set $F(x)=v_{x+x_0-i\Delta}(k)\,v_{x+x_0-i\Delta}(l)$. By Lemma 1, $|F(x)|\ll1/(1+|x-k|)(1+|x-l|)$, which is summable.
2. $F$ is the Fourier transform of $H(\sigma)=e^{2\pi\Delta\sigma}e^{2\pi i\sigma x_0}\int\psi(\xi)\psi(\sigma-\xi)e^{-2\pi i(\xi k+(\sigma-\xi)l)}d\xi$. This is continuous, supported in $[-1,1]$, and satisfies $H(\pm1)=0$ (the integration range degenerates to a point).
3. Poisson summation gives $\sum_mF(m)=\sum_nH(n)=H(0)=\int\psi(\xi)\psi(-\xi)e^{-2\pi i\xi(k-l)}d\xi$.
4. ψ is even, and the $+i\Delta$ member gives the same value. ∎

E5B wrote $A(\beta)=2\cosh(2\pi\beta\Delta)\sum_n\delta(\beta-n)$; that is shorthand for this entrywise statement. In the exact periodic model the identity is a finite-dimensional fact. Numerical check: experiment E2a gives ratio $0$ at spacing 1, to $10^{-15}$, for four windows.

## Theorem A′ (E5B finite-grid version) — identity PROVED, constant WITHDRAWN

E5B wrote $G^{\mathrm{seg}}=P(G_\infty-G^{\mathrm{out}})P$ for $d$ pairs at $0,\dots,d-1$ on the grid $\{0,\dots,d-1\}$, and claimed
$$\operatorname{tr}Q_-\le\frac{\zeta(3)}{4\pi^4}B_\psi(\Delta)^2\quad\text{uniformly in }d .$$

- **The identity is correct.** Entries converge absolutely, the out-term converges in trace norm, and $\operatorname{tr}(A-B)_-\le\|B\|_1$ for $A\succeq0$.
- **The constant is withdrawn.** The bound uses $|\hat g(s)|\le B/(2\pi s)^2$ with $B=\|g''\|_1$. For the paper's window, $\|\psi_L''\|_1\asymp L/w$, so $B\asymp e^{\pi\Delta}L/w$ is **not uniform as $T\to\infty$**. It is correct only for a fixed $C^2$ window independent of $L$.
- **Superseded by A″,** which is uniform in L.

## Theorem A″ (finite cluster inside a grid) — PROVED, [M]

**Statement.** Let $\Gamma\subset\mathbb Z$ be finite and $C=\{c_0,\dots,c_0+\ell-1\}\subseteq\Gamma$. Put pairs at $m\mp i\Delta$ for $m\in C$, and let $Q=P_\Gamma\mathbb G_CP_\Gamma$. Define
$$\beta=\sum_{m\in C}\ \sum_{k\in\mathbb Z\setminus C}|v_{m-i\Delta}(k)|^2 .$$
Then
$$\operatorname{tr}(Q_-)\ \le\ 4\beta+2\sqrt{\ell\,S_\psi(\Delta)\,\beta},\qquad \beta\le2c^2(2+\log\ell),$$
with $c$ from Lemma 1. Hence $\operatorname{tr}(Q_-)/\bigl(\ell(S_\psi(\Delta)-1)\bigr)=O_\Delta\bigl(\sqrt{\log\ell/\ell}\bigr)\to0$.

*Proof.* Split $\Gamma=C\sqcup C'$ and write $Q=\begin{pmatrix}X&Y\\Y^{\mathsf T}&Z\end{pmatrix}$. Since $\operatorname{tr}(\cdot)_-$ is subadditive and the off-diagonal part has eigenvalues $\pm\sigma_i(Y)$:
$$\operatorname{tr}Q_-\le\operatorname{tr}X_-+\operatorname{tr}Z_-+\|Y\|_1 .$$
1. **X-block.** $X=P_C\mathbb G_\infty P_C-P_C\mathbb G_{\mathbb Z\setminus C}P_C$. The first term is PSD by Theorem A. Hence
$$\operatorname{tr}X_-\le\|P_C\mathbb G_{\mathbb Z\setminus C}P_C\|_1\le\sum_{m\notin C}\sum_\pm\|P_Cv_m^\pm\|^2=2\sum_{m\notin C}\sum_{k\in C}|\hat g(m-k)|^2=2\beta .$$
   The trace norm of $aa^{\mathsf T}$ is $\|a\|^2$. The last equality uses $|\hat g(-s)|=|\hat g(s)|$.
2. **Z-block.** $\|Z\|_1\le\sum_{m\in C,\pm}\|P_{C'}v_m^\pm\|^2\le2\beta$.
3. **Off-diagonal block.** By Cauchy–Schwarz over $(m,\pm)$, using $\|P_Cv\|^2\le S_\psi(\Delta)$:
$$\|Y\|_1\le\sum_{m\in C,\pm}\|P_Cv\|\,\|P_{C'}v\|\le\sqrt{2\ell S}\,\sqrt{2\beta}.$$
4. **Bound on β.** For each $n\ge1$, the number of pairs $(m\in C,\ k\notin C)$ with $|m-k|=n$ is at most $2\min(n,\ell)$. So
$$\beta\le\sum_n2\min(n,\ell)\frac{c^2}{n^2}\le2c^2\Bigl[(1+\log\ell)+\ell\sum_{n>\ell}n^{-2}\Bigr]\le2c^2(2+\log\ell).\ ∎$$

**Assumptions to keep in view.**
- Pair centers lie on the grid lattice; any common offset is allowed by Theorem A, but distinct pairs must be at consecutive lattice points.
- $C\subseteq\Gamma$. If the cluster extends beyond the grid (as with $I'$ margins), use A′'s identity instead: with a margin $D$ beyond the grid, $\operatorname{tr}Q_-\le4dc^2/D$ by the same Lemma 1 decay.
- Multiplicity 1. With multiplicity $m$, both sides scale by $m$.

**Numerical consistency** (experiment E6, `e6_check.py`; grid 300, $\ell=100$):

| Window, Δ | $\operatorname{tr}Q_-$ | Bi-infinite $\operatorname{tr}(\mathbb G_C)_-$ | Bound | $\ell(S-1)$ |
|---|---|---|---|---|
| indicator, 0.5 | 13.93 | 15.84 | 122.2 | 267.6 |
| indicator, 1.0 | 338.95 | 389.45 | 2188.9 | 4161.3 |
| taper 0.1, 0.5 | 2.154 | 2.154 | 59.0 | 187.6 |

Re-run status (2026-10-19): the two indicator rows reproduce exactly. The taper row could not be re-run, because the script was killed for out-of-memory under an 8 GB cap; it currently rests on the original session's output only. See [experiments/README.md](../experiments/README.md). This is a consistency check, not part of the proof.

## Theorem B (density-one lattice) — PROVED in the periodic model; SKETCHED elsewhere

For pairs at spacing 2 (zero density 1), the negative mass per pair satisfies
$$\frac{\operatorname{tr}Q_-}{\#\text{pairs}}\le e^{\pi\Delta}-1\qquad\text{for every window}.$$

*Proof (periodic model).* The Fourier classes have size at most 2, and each contributes the matrix $(1/s)(xy^{\mathsf T}+yx^{\mathsf T})$ with $x_n=\psi_ne^{an}$, $y_n=\psi_ne^{-an}$, $a=\pi\Delta$. Its negative eigenvalue is $(|x||y|-x\cdot y)/s$, and
$$|x|^2|y|^2=(\psi_0^2+\psi_1^2e^{2a})(\psi_0^2+\psi_1^2e^{-2a})\le e^{2a}(\psi_0^2+\psi_1^2)^2 .$$
Sum over classes. ∎

For the indicator the value is exactly $\cosh\pi\Delta-1$, so the ratio to $S-1$ is about $2\pi\Delta\,e^{-\pi\Delta}\to0$.
- Continuum and finite-segment versions: SKETCHED (compression argument as in A″, not written out).
- Clusters of 30, 100, 250, 500 pairs converge to the lattice value (E5b): NUMERICALLY TESTED.
