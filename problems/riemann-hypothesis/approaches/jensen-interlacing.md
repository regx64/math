# Jensen polynomials and root interlacing

**Source.** The separate claude.ai conversation "Jensen polynomial interlacing for Riemann hypothesis" (chat `15786f47`, 2026-10-19 00:43 KST, same project). Statements are transcribed from its final reply. The code was **recovered verbatim from the transcript** and re-run here: [../experiments/code/jensen-interlacing](../experiments/code/jensen-interlacing).

## Idea

For $\Xi(z)=\sum(-1)^n\gamma_nz^{2n}$, the Pólya–Jensen criterion says RH holds iff every Jensen polynomial $J_{d,n}(x)=\sum_j\binom dj\gamma(n+j)x^j$ is hyperbolic. The proposal: use the recurrence
$$J_{d,n}=J_{d-1,n}+xJ_{d-1,n+1}$$
and root interlacing to propagate hyperbolicity from large shifts, where GORZ and GORTTW apply, down to small shifts.

## Results

| ID | Statement | Status |
|---|---|---|
| JEN-1 | **Normalization correction.** Pólya's criterion needs $\gamma(n)=8\,n!\,\gamma_n$. With raw Taylor coefficients the criterion is implied by RH but not equivalent to it (toy example: $1+2x+2x^2$ versus $(1+x)^2$). | PROVED (remark); standard normalization from GORZ |
| JEN-2 | $J_{d,n}=J_{d-1,n}+xJ_{d-1,n+1}$ and $J_{d,n}'=dJ_{d-1,n+1}$ | PROVED (re-checked) |
| JEN-3 | **Interlacing lemma.** For $\gamma_k>0$: the pattern $b_1<a_1<\dots<a_{d-1}<b_d=0$ holds iff $J_{d,n}$ has $d$ simple real zeros, where the $a$'s are the zeros of $J_{d-1,n}$ and the $b$'s those of $xJ_{d-1,n+1}$. Key identity: $B=xJ'/d$ and $A=J-B$. | PROVED (re-read in consolidation); almost certainly folklore |
| JEN-4 | **Counterexample to propagation.** Kernel $e^{-u^2}(1+u^4/2)$ gives $F(x)=e^{x/4}(x^2+12x+44)$. Then $J^*_{d,0}\propto y^{d-2}(44y^2+12dy+d(d-1))$, whose discriminant $16d(11-2d)$ is negative for $d\ge6$. Since $F'\in\mathcal{LP}$, all $J_{d,n}$ with $n\ge1$ are hyperbolic. So positivity, Turán, all $d\le5$, and all shifts $n\ge1$ hold, yet shift 0 fails. | PROVED (discriminant re-checked); exact root counts re-run. **Caveat found in the re-run:** in this example the $J_{d,n}$ have **multiple** real zeros (for example $J_{4,0}$ has a double root at −4; `ce2.py`'s distinct-root Sturm count flags $d=4$, $n=0..7$). So the example refutes backward propagation of *hyperbolicity*. It does not refute a version that assumes *simple* zeros at the shifts $n\ge1$, which is what JEN-5's hypothesis needs. |
| JEN-5 | **Induction theorem.** $J_{d,n}$ has simple real zeros iff $J_{d-1,n}$ and $J_{d-1,n+1}$ do and their zeros strictly interlace | SKETCHED. The source calls it proved; it was not re-derived during consolidation. |
| JEN-6 | All $J_{d,n}$ for $2\le d\le14$ and $0\le n\le25$ (338 cases) are hyperbolic with simple zeros, using 80-digit Ξ coefficients | NUMERICALLY TESTED (re-run status in experiments) |
| JEN-7 | Verdict: the approach is a reformulation of RH; no intermediate step becomes easier | assessment |

## Obstruction

The propagation hypothesis at level $d-1$ *is* hyperbolicity at level $d$. JEN-4 shows that backward propagation in $n$ needs input specific to ξ, beyond positivity, kernel shape or low-degree Turán inequalities.

## Literature (as cited in the source)

- Griffin–Ono–Rolen–Zagier, PNAS 2019 (arXiv:1902.07321).
- GORTTW, Adv. Math. 2022 (arXiv:1910.01227).
- Farmer, arXiv:2008.07206 (Jensen polynomials are not a plausible route).
- Csordas–Norfolk–Varga 1986; Dimitrov–Lucas 2011.
- The Craven–Csordas simplicity reference was flagged in the source as **not verified**.
