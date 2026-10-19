# RT+, Theorem S and Theorem NL

## RT+ (rank–trace with slack kept) — PROVED, [M]

**Statement.** Let $P\succeq0$ with $\operatorname{rank}P\le r$. Let $Q=Q_+-Q_-$ with $Q_\pm\succeq0$, $Q_+Q_-=0$ and $\operatorname{rank}Q_+\le b$. Then
$$r\ \ge\ 2\operatorname{tr}P+4\operatorname{tr}Q-4b-\|P+Q\|_F^2\;+\;2\operatorname{tr}Q_-\;+\sum_{q\in\operatorname{spec}(Q_+)\setminus\{0\}}(q-2)^2 .$$

*Proof (re-derived twice: in P8 and again for this archive).*
1. Expand $\|P+Q\|^2=\|P\|^2+\|Q_+\|^2+\|Q_-\|^2+2\operatorname{tr}(PQ_+)-2\operatorname{tr}(PQ_-)$.
2. Von Neumann's trace inequality gives $\operatorname{tr}(PQ_-)\le\sum_ip_in_i$, with eigenvalues in decreasing order.
3. For $i\le r$: $(p_i-n_i)^2=(p_i-n_i-1)^2+(2p_i-1-4n_i)+2n_i$.
4. For $i>r$, where $p_i=0$: $n_i^2=-4n_i+(n_i^2+4n_i)$, and $n_i^2+4n_i\ge2n_i$.
5. For the positive part: $q^2=4q-4+(q-2)^2$.
6. Dropping $2\operatorname{tr}(PQ_+)\ge0$ and the von Neumann gap gives the claim. ∎

With the slack terms removed, this is Alpöge–Furman Lemma 3.2, which is the $c=2$ case of the formal `rank_trace_ineq` (`Zeta23/LinAlg/RankTrace.lean:163`).

## Theorem S — SKETCHED

**Statement.** With the paper's analytic inputs (window ψ, $\lambda=1$), let $P_1$ be the simple on-line part and $Q'=\hat A-P_1$. Then
$$2\operatorname{tr}(Q'_-)\le(R(\psi)-1)N-2p-m_2+o(N).$$

*Argument.*
- Apply RT+ with $\operatorname{tr}\hat A=N+o(N)$, $\|\hat A\|^2=RN+o(N)$, $\operatorname{tr}P_1+2n_+(Q')\le N$, and $\operatorname{rank}P_1\le N_0^s\le N-2p-m_2$.
- $\operatorname{tr}(\cdot)_-$ is 1-Lipschitz in trace norm, so the paper's $o(N)$ trace-norm tail (`TailInputs`) costs $o(N)$.

*Why SKETCHED.*
- The paper's assembly (how $\hat E$, the edge effects and the units enter) was not re-derived line by line for the slack version.
- The original P7 statement also kept $\sum_{\lambda>0}(\lambda-2)^2$ on the left. That term is **WITHDRAWN**: it is not stable under a trace-norm perturbation when the eigenvalues are of size $e^{2\pi\Delta}$.

**Corollary (pairs only) — SKETCHED.** Since $Q'=Q^{\mathrm{pairs}}+M$ with $M\succeq0$ and $\operatorname{tr}M=m_2$, we have $\operatorname{tr}Q^{\mathrm{pairs}}_-\le\operatorname{tr}Q'_-+m_2$. Hence
$$\operatorname{tr}Q^{\mathrm{pairs}}_-\le\tfrac12\bigl[(R-1)N-2p+m_2\bigr]+o(N)\le(R-1)N-2p+o(N).$$
The second inequality uses $2p+m_2\le(R-1)N+o(N)$.

## Theorem NL — WITHDRAWN

The P7 statement is reproduced in [01-original-conjecture.md](01-original-conjecture.md).
- It was conditional on AC, which is refuted for [M] and [D].
- Theorem C shows that NL cannot follow from Theorem S's inputs at all.
- Even under extra density hypotheses, Theorem B limits this route to decay of order $e^{-\pi\Delta}$. Jutila's known estimate already gives $e^{-2\pi c\Delta}$ for every $c<1$.

**Whether any near-line density bound follows from the full bandwidth-one pair-correlation data is OPEN** (AC_F).
