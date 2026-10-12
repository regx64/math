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

## 다음
가우스 소거법, 행렬식, 랭크, 고유값·고유벡터, 내적공간
