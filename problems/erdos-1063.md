# Erdős #1063 — $k$가 소수인 경우

**문제.** $k\ge2$에 대해 $n_k\ge2k$를, $0\le i<k$ 중 단 하나를 빼고 모두 $n-i\mid\binom nk$가 되는 가장 작은 $n$이라 하자. $n_k$를 추정하라. ([erdosproblems.com/1063](https://www.erdosproblems.com/1063))

**기존 결과.** Monier(1985) $n_k\le k!$, Cambie $n_k\le k\cdot\operatorname{lcm}(2,\dots,k-1)=e^{(1+o(1))k}$. 소수 $k=p$에 대한 하한은 $n_p\ge p$ 정도뿐.

**여기서 얻은 것 (2026-10-12).** $k=p$ 소수일 때
1. 정확한 판정 조건
2. 무조건 하한 $n_p\ge p^{11/6-\varepsilon}$ (Jia 정리를 쓰면 $p^{39/20-\varepsilon}$, RH 가정 시 $p^{2-o(1)}$)
3. 휴리스틱 $\log n_p\asymp p/\log p$ — 다항식으로는 안 묶일 것

전체 증명: [pdf/erdos1063-prime-k.pdf](../pdf/erdos1063-prime-k.pdf) (소스 `latex/erdos1063-prime-k.tex`)

## 1. 판정 조건
$n=Mp+i_0$ ($0\le i_0<p$)로 쓴다.

- 쿰머 정리 $v_q\binom np=\#\{j\ge1: n\bmod q^j<p\bmod q^j\}$에서 $v_p\binom np=v_p(n-i_0)-1$. 그래서 빠지는 $i$는 항상 $i_0=n\bmod p$.
- $q<p$에 대해 $L_q=\lfloor\log_qp\rfloor$, $e_q=\max_iv_q(n-i)$, $e_q^*=\max_{i\ne i_0}v_q(n-i)$, $D_q=\#\{1\le j\le L_q:n\bmod q^j\ge p\bmod q^j\}$로 두면 $v_q\binom np=e_q-D_q$.

> **정리.** $n\ge2p$가 조건을 만족 $\iff$ 모든 소수 $q<p$에 대해 $D_q=0$ 또는 $v_q(n-i_0)\ge e_q^*+D_q$.

$q\in(p/2,p)$이면 "$n\bmod q<p-q$ 또는 $q\mid M$"으로 단순해진다.

검증: $p\in\{5,\dots,23\}$, $2p\le n<20000$인 139,810쌍에서 직접 계산과 전부 일치.

## 2. 하한
$q=p-g$가 $(p/2,p)$의 소수이고 $M<p/2$이면, $q$가 조건을 만족하는 것은

$$
g\in\bigcup_{j\ge1}\Big[\tfrac{jp-i_0}{M+j},\ \tfrac{jp-i_0}{M+j-1}\Big)
$$

일 때뿐이다($p<200$에서 2,091,482개 경우 확인). 이 구간들 사이의 틈 $J_j$($1\le j\le M/4$)에는 소수 $p-g$가 있으면 안 되고, 각 틈의 길이는

$$
a_{j+1}-b_j=\frac{p(M-1-j)+2i_0}{(M+j+1)(M+j-1)}\ \ge\ \frac{2p}{9M}.
$$

틈이 약 $M/4$개라 $(p/2,p)$의 일정 비율이 소수 없는 구간으로 덮인다. Huxley(1972): 거의 모든 $(x,x+x^{\theta}]$ ($\theta>1/6$)에 소수가 있음. 따라서 $M\gtrsim p^{1-\theta}$, 즉

$$
n_p\ \ge\ \frac{p^{2-\theta}}{10}\quad\Longrightarrow\quad n_p\ge p^{11/6-\varepsilon}.
$$

| 쓰는 정리 | 하한 |
|---|---|
| Baker–Harman–Pintz (틈 하나만) | $p^{1.475}/13$ |
| Huxley (1972), $\theta>1/6$ | $p^{11/6-\varepsilon}$ |
| Jia (1996), $\theta>1/20$ | $p^{39/20-\varepsilon}$ |
| R. Li 프리프린트 (미검증), $\theta>1/21.5$ | $p^{2-2/43-\varepsilon}$ |
| RH (Selberg) | $p^{2-o(1)}$ |

$M\ge p$가 되면 틈 길이가 1 미만이라 이 논법은 $p^2$에서 멈춘다.

## 3. 데이터

| $p$ | $n_p$ | $M$ | $i_0$ | $\log n_p$ | $\log n_p/\pi(p)$ |
|---|---|---|---|---|---|
| 5 | 12 | 2 | 2 | 2.48 | 0.83 |
| 7 | 30 | 4 | 2 | 3.40 | 0.85 |
| 11 | 280 | 25 | 5 | 5.63 | 1.13 |
| 13 | 210 | 16 | 2 | 5.35 | 0.89 |
| 17 | 1456 | 85 | 11 | 7.28 | 1.04 |
| 19 | 612 | 32 | 4 | 6.42 | 0.80 |
| 23 | 2640 | 114 | 18 | 7.88 | 0.88 |
| 29 | 34776 | 1199 | 5 | 10.46 | 1.05 |
| 31 | 8100 | 261 | 9 | 9.00 | 0.82 |
| 37 | 665280 | 17980 | 20 | 13.41 | 1.12 |
| 41 | 1154440 | 28157 | 3 | 13.96 | 1.07 |

OEIS A389360의 $a(43)=24458112$, $a(47)=3076480$도 비율 1.21, 1.00.

## 새로운 결과인가
문제 페이지, 수정 이력, 포럼, OEIS A389360에는 소수 $k$에서 $p$를 넘는 하한이 없음. Erdős–Selfridge(1983), Monier(1985), Guy B31 원문은 확인 못 함. 판정 조건의 앞부분은 표준적인 쿰머/뤼카 계산일 가능성이 높고, 새로 보태는 건 하한과 휴리스틱. 증명은 독립 검토 전.
