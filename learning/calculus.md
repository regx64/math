# 미적분 → 다변수 미적분

목표: 비압축성 나비에–스토크스 방정식을 수학적으로 읽을 수 있는 수준.

$$
\rho\left(\frac{\partial \mathbf u}{\partial t}+(\mathbf u\cdot\nabla)\mathbf u\right)=-\nabla p+\mu\nabla^2\mathbf u+\mathbf f,\qquad \nabla\cdot\mathbf u=0
$$

로드맵: 1변수 미적분 → 다변수 미적분 → 벡터 미적분 → ODE/PDE → 선형대수

## 한 것

### 1변수
- 극한: 대입하면 $0/0$이 되는 경우 인수분해로 처리, 좌극한·우극한
- 연속: $\lim_{x\to a}f(x)=f(a)$. 좌극한 $=$ 우극한은 극한이 **존재**한다는 뜻일 뿐이고, 연속이려면 $f(a)$가 정의되어 있고 그 값과 같아야 함
- 미분계수: $f'(a)=\lim_{h\to0}\dfrac{f(a+h)-f(a)}{h}$ — 할선 기울기가 접선 기울기로 수렴
- 도함수 규칙: 거듭제곱, 곱의 법칙, 연쇄법칙 $\big(f(g(x))\big)'=f'(g(x))\,g'(x)$
- 활용: 증가·감소, 극값, 부호표
- 부정적분, 정적분, 미적분학의 기본정리 $\dfrac{d}{dx}\displaystyle\int_a^x f(t)\,dt=f(x)$

### 다변수
- 편미분, 다변수 연쇄법칙
- 이계편미분, Clairaut 정리 $f_{xy}=f_{yx}$ (2계 편도함수가 연속일 때)
- 벡터장, 그래디언트 $\nabla f$ (등고선에 수직, 가장 가파른 오르막 방향)
- 발산 $\nabla\cdot\mathbf F=\partial_xF_1+\partial_yF_2+\partial_zF_3$
- 회전 $\nabla\times\mathbf F=(\partial_yF_3-\partial_zF_2,\ \partial_zF_1-\partial_xF_3,\ \partial_xF_2-\partial_yF_1)$
- 다변수 극값: 임계점, 안장점, 이차미분판정법 $D=f_{xx}f_{yy}-f_{xy}^2$

### 나비에–스토크스와의 연결
| 항 | 수학 |
|---|---|
| $-\nabla p$ | 압력의 그래디언트 |
| $\mu\nabla^2\mathbf u$ | 라플라시안 (점성) |
| $\nabla\cdot\mathbf u=0$ | 발산 0 (비압축) |
| $(\mathbf u\cdot\nabla)\mathbf u$ | 대류항, 연쇄법칙에서 나옴 |

## 자주 한 실수
- 연쇄법칙에서 안쪽 함수의 미분을 빠뜨림
- 회전 공식에서 항 순서를 반대로 적용
- 연립방정식 대입 계산 실수 → 암산 말고 종이에 쓰기

## 다음
그래디언트·라플라시안·회전의 관계를 묻는 종합 문제. 예: $\nabla\times(\nabla f)=\mathbf 0$, $\nabla\cdot(\nabla\times\mathbf F)=0$, $\nabla\cdot(\nabla f)=\nabla^2 f$.
