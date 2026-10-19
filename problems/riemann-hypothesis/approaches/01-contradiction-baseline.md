# 01 — Proof by contradiction: formal setup and what established results give

**Phase P0** (2026-10-18 23:51 KST), main conversation, first reply. **Scope [ζ].**

## Idea

Assume an off-line nontrivial zero $s_0=\sigma_0+it_0$ with $\sigma_0\ne\tfrac12$, and test it against the standard toolkit: the functional equation, symmetries, the Euler product, zero-free regions, zero counting, zero density, numerical verification, and equivalent criteria.

## Formal statement

The proposition as written needs the pole excluded:
$$\mathrm{RH}:\ \forall s\in\mathbb C\setminus(2\mathbb Z^-\cup\{1\}),\ \zeta(s)=0\Rightarrow\operatorname{Re}s=\tfrac12 .$$
Equivalently, every zero of $\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ satisfies $\operatorname{Re}s=\tfrac12$.

## Derived consequences of an off-line zero (claim BASE-1)

1. $0<\sigma_0<1$, by the Euler product, Hadamard–de la Vallée Poussin, and the functional equation with the Γ-poles.
2. $t_0\ne0$: on $(0,1)$, $\zeta(\sigma)=\eta(\sigma)/(1-2^{1-\sigma})<0$.
3. $\{s_0,\bar s_0,1-s_0,1-\bar s_0\}$ are four distinct zeros.
4. $|t_0|>3\cdot10^{12}$ (Platt–Trudgian).
5. $\sigma_0<1-c/\bigl((\log t_0)^{2/3}(\log\log t_0)^{1/3}\bigr)$ (Vinogradov–Korobov). The constant $c=1/57.54$ attributed to Ford was **not re-checked**.

## Where it stops (claim BASE-2)

The admissible region
$$\mathcal C=\Bigl\{t>3\cdot10^{12},\ \tfrac12<\sigma<1-\tfrac{c}{(\log t)^{2/3}(\log\log t)^{1/3}}\Bigr\}$$
is nonempty. Proving it zero-free is exactly RH.

Structural reason: the Davenport–Heilbronn function has a functional equation and growth of the same type, but no Euler product, and it has infinitely many zeros with $\operatorname{Re}s>1$. So an argument that uses only the functional equation, continuation and growth cannot succeed.

## Strongest surviving result

The constraint list above, which is standard. No contradiction was derived.

## Side remark (claim BASE-3, UNVERIFIED)

RH is a $\Pi^0_1$ statement (via Lagarias' criterion), so it cannot be independent of ZFC and false at the same time. This was stated as standard and not re-derived.

## Literature

Platt–Trudgian (2021), Ford (2002), Davenport–Heilbronn (1936), Conrey (1989), Guth–Maynard (2024). See [../external-results.md](../external-results.md) for how each citation was checked.
