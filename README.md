# math

regx64(hoon)가 직접 공부하고 시도한 수학 기록.

- `learning/` — 학습 노트 (Markdown, 수식은 LaTeX)
- `problems/` — 미해결 문제 시도와 결과
- `problem-sets/` — 커뮤니티 배포용 문제집 (풀이 포함)
- `latex/` — 같은 내용의 LaTeX 소스
- `pdf/` — 컴파일된 PDF
- `materials/` — 채팅에서 만든 교재·공식집·영상 원본 (푸리에 교재 103쪽, 도형의 방정식 공식집 3종, 접선 유도 영상)
- `lean/` — Lean 4 검증 파일

## 학습

| 주제 | 시작 | 상태 | 노트 |
|---|---|---|---|
| 1변수·다변수 미적분 (나비에–스토크스 로드맵) | 2026-10 | 다변수 극값까지 완료, 종합 문제 차례 | [calculus.md](learning/calculus.md) |
| 푸리에 변환 | 2026-10-10 | 교재 0장(삼각함수) 진행 중 | [fourier-transform.md](learning/fourier-transform.md) |
| 선형대수 | 2026-10-09 | 시작 단계 | [linear-algebra.md](learning/linear-algebra.md) |
| P vs NP | 2026-10 | 다항·지수 시간까지, 다음은 NP-완전 | [p-vs-np.md](learning/p-vs-np.md) |
| 도형의 방정식 | 2026-09 | 접선 공식 유도·Lean 검증, 내심·외심, 원다발 | [analytic-geometry.md](learning/analytic-geometry.md) |
| 이산수학 (논리) | 2026-09-28 | 명제논리·술어논리 | [discrete-math.md](learning/discrete-math.md) |
| 집합과 경우의 수 | 2026-09-29 | 씨름용 문제 2개 풀이 | [combinatorics.md](learning/combinatorics.md) |
| 지수의 확장 | 2026-08-23 | 유리수·무리수 지수 | [exponents.md](learning/exponents.md) |
| Shapley value | 2026-10-01 | 정의·예제·연습문제 | [shapley-value.md](learning/shapley-value.md) |
| 힐베르트 11번·24번 | 2026-10-03 | 국소–대역 원리 (종 버전) 증명 | [hilbert-problems.md](learning/hilbert-problems.md) |
| Lean 형식화 | 2026-08-21 | 개념 정리 | [lean.md](learning/lean.md) |

## 문제 시도

| 문제 | 결과 | 노트 |
|---|---|---|
| Erdős #1063 ($k$가 소수) | 판정 조건 + 하한 $n_p\ge p^{11/6-\varepsilon}$ 증명 | [erdos-1063.md](problems/erdos-1063.md), [PDF](pdf/erdos1063-prime-k.pdf) |
| Erdős #1110 ($\{2,9\}$) | $9^a-2$ 부분 결과, 증명 미완 | [erdos-1110.md](problems/erdos-1110.md) |
| Erdős #1212 | 두 경로 모두 막힘 | [erdos-1212.md](problems/erdos-1212.md) |
| 퍼콜레이션 임계값 주장 검토 | 핵심 결과는 Harris–Kesten의 따름정리 | [percolation-claim-review.md](problems/percolation-claim-review.md) |
| $3\times3$ 행렬곱 rank ($\mathbb F_2$) | flip 탐색으로 22 없음, 하한 확장의 다음 지점 특정 | [matrix-mult-3x3.md](problems/matrix-mult-3x3.md) |
| 리만 가설 (2026-10-18~19) | 증명 아님. 방법의 한계 결과(Landau 상수, 분해능 장벽, AC 반박·Theorem A″), 철회된 주장 표시, AC_F 미해결 | [riemann-hypothesis/README.md](problems/riemann-hypothesis/README.md) (영문 아카이브) |
| 직접 만든 문제 | 덧셈·XOR 동시 Sidon, 작은 계수 컨볼루션 | [original-problems.md](problems/original-problems.md) |
| 난제 후보 | 미선택 | [candidates.md](problems/candidates.md) |

## 문제집

| 문제집 | 노트 |
|---|---|
| 대수학 (석사 수준) 5문제 | [algebra-graduate.md](problem-sets/algebra-graduate.md) |
| 대수학 (학사 수준, 재밌는 것) 5문제 | [algebra-undergraduate.md](problem-sets/algebra-undergraduate.md) |
| 토론용 기하 5문제 | [geometry-discussion.md](problem-sets/geometry-discussion.md) |

## PDF

- [pdf/learning-notes.pdf](pdf/learning-notes.pdf) — 학습 노트 전체
- [pdf/problem-notes.pdf](pdf/problem-notes.pdf) — 문제 시도 전체 (한국어)
- [pdf/problem-sets.pdf](pdf/problem-sets.pdf) — 문제집 전체
- [pdf/erdos1063-prime-k.pdf](pdf/erdos1063-prime-k.pdf) — #1063 증명 노트 (영문)

빌드: `sh latex/md2tex.sh && cd latex && make` (Markdown 노트 일부를 `latex/gen/`으로 변환한 뒤 컴파일)
