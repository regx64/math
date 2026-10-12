# 선형대수

시작: 2026-10-09. 기한 없이 전 분야를 다루는 게 목표.

시작 시점 수준: 연립방정식은 풀 수 있지만 행렬로 푸는 법은 모름.

## 지금까지 본 개념 (푸리에 교재 2장과 겹침)

- 선형결합, $\operatorname{span}$, 일차독립
- 기저와 차원. 기저가 정해지면 좌표는 유일하다.
- 행렬–벡터 곱은 열들의 선형결합:

$$
A\mathbf x=x_1\mathbf a_1+x_2\mathbf a_2+\cdots+x_n\mathbf a_n
$$

- 연립방정식 $c_1+c_2=5,\ c_1-c_2=1$은 $B\mathbf c=\mathbf x$ 한 줄:

$$
\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}3\\2\end{pmatrix}=\begin{pmatrix}5\\1\end{pmatrix}
$$

- 선형변환 $L(a\mathbf x+b\mathbf y)=aL(\mathbf x)+bL(\mathbf y)$. 행렬 곱 $AB$는 "$B$ 다음 $A$". 일반적으로 $AB\ne BA$.
- 역행렬이 있으면 $A\mathbf x=\mathbf b\Rightarrow\mathbf x=A^{-1}\mathbf b$

## 응용: 페이지랭크 (2026-08-31)
페이지랭크는 행렬 계산이 정의 자체다.

- 전이행렬 $M$: 페이지 $j$가 링크 $L_j$개를 가지면 $M_{ij}=1/L_j$ ($j\to i$ 링크가 있을 때). 열의 합이 1.
- 감쇠계수 $d$ (보통 0.85)를 넣은 구글 행렬

$$
G=dM+\frac{1-d}{n}\mathbf 1\mathbf 1^{\top}
$$

- 페이지랭크 벡터 $\mathbf r$은 고유값 1에 대한 고유벡터: $G\mathbf r=\mathbf r$, $\sum r_i=1$
- 계산은 거듭제곱법: $\mathbf r_{t+1}=dM\mathbf r_t+\frac{1-d}{n}\mathbf 1$을 수렴할 때까지 반복
- 실제 웹 규모에서는 $M$을 희소행렬로 저장

예: 링크 $1\to2,\ 1\to3,\ 2\to3,\ 3\to1$, $d=0.85$이면 $\mathbf r\approx(0.388,\ 0.215,\ 0.397)$. $G$의 나머지 고유값은 $-0.425\pm0.425i$ (크기 약 0.60)라서 반복할 때마다 오차가 약 0.6배로 줄어든다.

## 다음
가우스 소거법, 행렬식, 랭크, 고유값·고유벡터, 내적공간
