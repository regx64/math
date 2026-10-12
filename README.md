# math

regx64(hoon)가 직접 공부하고 시도한 수학 기록.

- `learning/` — 학습 노트 (Markdown, 수식은 LaTeX)
- `problems/` — 미해결 문제 시도와 결과
- `latex/` — 같은 내용의 LaTeX 소스
- `pdf/` — 컴파일된 PDF

## 학습

| 주제 | 시작 | 상태 | 노트 |
|---|---|---|---|
| 1변수·다변수 미적분 (나비에–스토크스 로드맵) | 2026-10 | 다변수 극값까지 완료, 종합 문제 차례 | [calculus.md](learning/calculus.md) |
| 푸리에 변환 | 2026-10-10 | 교재 0장(삼각함수) 진행 중 | [fourier-transform.md](learning/fourier-transform.md) |
| 선형대수 | 2026-10-09 | 시작 단계 | [linear-algebra.md](learning/linear-algebra.md) |
| P vs NP | 2026-10 | 다항·지수 시간까지, 다음은 NP-완전 | [p-vs-np.md](learning/p-vs-np.md) |
| 도형의 방정식 | 2026-09 | 접선 공식 유도·Lean 검증 | [analytic-geometry.md](learning/analytic-geometry.md) |

## 문제 시도

| 문제 | 결과 | 노트 |
|---|---|---|
| Erdős #1063 ($k$가 소수) | 판정 조건 + 하한 $n_p\ge p^{11/6-\varepsilon}$ 증명 | [erdos-1063.md](problems/erdos-1063.md), [PDF](pdf/erdos1063-prime-k.pdf) |
| Erdős #1110 ($\{2,9\}$) | $9^a-2$ 부분 결과, 증명 미완 | [erdos-1110.md](problems/erdos-1110.md) |
| Erdős #1212 | 두 경로 모두 막힘 | [erdos-1212.md](problems/erdos-1212.md) |
| 퍼콜레이션 임계값 주장 검토 | 핵심 결과는 Harris–Kesten의 따름정리 | [percolation-claim-review.md](problems/percolation-claim-review.md) |

## PDF

- [pdf/learning-notes.pdf](pdf/learning-notes.pdf) — 학습 노트 전체
- [pdf/problem-notes.pdf](pdf/problem-notes.pdf) — 문제 시도 전체 (한국어)
- [pdf/erdos1063-prime-k.pdf](pdf/erdos1063-prime-k.pdf) — #1063 증명 노트 (영문)

빌드: `cd latex && make`
