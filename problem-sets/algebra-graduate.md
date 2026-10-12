# 대수학 문제 (석사 수준)

2026-10-10. 커뮤니티 배포용. 난이도: 1·2 기본, 3·4 중간, 5 계산 포함.

## 1. 군론
$G$를 유한군, $p$를 $|G|$의 가장 작은 소인수라 하자. $[G:H]=p$인 부분군 $H$는 정규부분군임을 보여라.

**풀이.** $G$가 좌잉여류 집합 $G/H$($p$개)에 작용해 준동형 $\varphi:G\to S_p$가 생긴다. $K=\ker\varphi\subseteq H$. $G/K\hookrightarrow S_p$이므로 $|G/K|$는 $p!$와 $|G|$의 공약수다. $|G|$의 소인수는 모두 $p$ 이상이고, $p!$에서 $p$ 이상인 소인수는 $p$ 하나뿐이며 지수가 1이므로 $|G/K|\mid p$. 한편 $[G:K]=p\,[H:K]$이므로 $[H:K]=1$, 즉 $H=K\trianglelefteq G$. $\blacksquare$

## 2. 환론
$R$을 가환환, $f=a_0+a_1x+\cdots+a_nx^n\in R[x]$라 하자. $f$가 단원 $\iff$ $a_0\in R^\times$이고 $a_1,\dots,a_n$이 모두 멱영원.

**풀이.** ($\Leftarrow$) 멱영원의 합은 멱영원이고, 단원 + 멱영원은 단원이다.
($\Rightarrow$) $fg=1$이면 상수항에서 $a_0\in R^\times$. 임의의 소아이디얼 $P$에 대해 $R/P$는 정역이므로 $(R/P)[x]$의 단원은 상수뿐이다. 따라서 $i\ge1$에서 $a_i\in P$. 모든 소아이디얼의 교집합은 $\operatorname{nil}(R)$이므로 $a_i$는 멱영원. $\blacksquare$

## 3. 갈루아 이론
$f(x)=x^4-4x^2+2$의 $\mathbb Q$ 위 갈루아 군을 구하여라.

**풀이.** 2에 대한 아이젠슈타인으로 기약. 근은 $\pm\alpha,\pm\alpha'$, $\alpha=\sqrt{2+\sqrt2}$, $\alpha'=\sqrt{2-\sqrt2}$. $\sqrt2=\alpha^2-2$, $\alpha\alpha'=\sqrt2$이므로

$$
\alpha'=\frac{\alpha^2-2}{\alpha}\in\mathbb Q(\alpha)
$$

라서 분해체는 $\mathbb Q(\alpha)$, 군의 위수는 4. $\sigma(\alpha)=\alpha'$이면 $\sigma(\sqrt2)=-\sqrt2$이고

$$
\sigma(\alpha')=\frac{\alpha'^2-2}{\alpha'}=\frac{-\sqrt2}{\alpha'}=-\alpha
$$

즉 $\alpha\mapsto\alpha'\mapsto-\alpha\mapsto-\alpha'\mapsto\alpha$로 위수 4. $\operatorname{Gal}\cong\mathbb Z/4\mathbb Z$. $\blacksquare$

## 4. 가군 / 표준형
$A\in M_n(\mathbb Q)$, $A^3=I$인 행렬의 닮음류는 몇 개인가?

**풀이.** 최소다항식은 $x^3-1=(x-1)(x^2+x+1)$의 약수이고 중근이 없어 가군이 반단순이다.

$$
\mathbb Q^n\cong\big(\mathbb Q[x]/(x-1)\big)^a\oplus\big(\mathbb Q[x]/(x^2+x+1)\big)^b,\qquad a+2b=n
$$

닮음류는 $(a,b)$와 일대일 대응하므로 $\lfloor n/2\rfloor+1$개. $\blacksquare$

## 5. 유한체
$I_n(q)$를 $\mathbb F_q$ 위 $n$차 일계수 기약다항식의 개수라 하자.

$$
I_n(q)=\frac1n\sum_{d\mid n}\mu(d)\,q^{n/d}
$$

을 증명하고 $I_6(2)$를 구하여라.

**풀이.** $x^{q^n}-x$는 중근이 없고(도함수 $-1$), 차수가 $n$의 약수인 모든 일계수 기약다항식의 곱이다. 차수를 비교하면 $q^n=\sum_{d\mid n}d\,I_d(q)$이고 뫼비우스 반전으로 결론. $\blacksquare$

$$
I_6(2)=\tfrac16\big(2^6-2^3-2^2+2\big)=9
$$
