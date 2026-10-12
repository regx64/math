/-
  원 밖의 점에서 그은 접선 공식 검증 (Lean 4 core, Mathlib 없음)
  원: x² + y² = r², 원 밖의 점 P(p, q), l² = p² + q² − r², s² = 1 (부호 ±)
  접선: r(px + qy) + s·l(py − qx) = r(p² + q²)
  모든 정리는 임의의 가환환 α에서 성립하므로 ℝ에서도 성립한다.
-/
open Lean.Grind

variable {α : Type} [CommRing α]

/-- 법선벡터 n = (n₁, n₂) -/
def n1 (r p q l s : α) : α := r*p - s*l*q
def n2 (r p q l s : α) : α := r*q + s*l*p

/-- (0) 문서의 공식은 n₁x + n₂y = r(p²+q²)와 같은 직선이다. -/
theorem formula_eq (r p q l s x y : α) :
    r*(p*x + q*y) + s*l*(p*y - q*x) = n1 r p q l s * x + n2 r p q l s * y := by
  unfold n1 n2; grind

/-- (1) 직선이 점 P(p, q)를 지난다. -/
theorem passes_P (r p q l s : α) :
    n1 r p q l s * p + n2 r p q l s * q = r*(p*p + q*q) := by
  unfold n1 n2; grind

/-- (2) |n|² = (p²+q²)². 따라서 원점에서 직선까지 거리 = r(p²+q²)/(p²+q²) = r. -/
theorem normal_sq (r p q l s : α)
    (hl : l*l = p*p + q*q - r*r) (hs : s*s = 1) :
    n1 r p q l s ^ 2 + n2 r p q l s ^ 2 = (p*p + q*q)^2 := by
  unfold n1 n2; grind

/-- (2') 거리 조건을 제곱한 형태: (r·d²)² = r²·|n|² -/
theorem dist_eq_r (r p q l s : α)
    (hl : l*l = p*p + q*q - r*r) (hs : s*s = 1) :
    (r*(p*p + q*q))^2 = r^2 * (n1 r p q l s ^ 2 + n2 r p q l s ^ 2) := by
  rw [normal_sq r p q l s hl hs]; grind

/-- 핵심 항등식 (가설 없음): 접점 판정용 -/
theorem key_identity (r p q l s x y : α) :
    ((p*p+q*q)*x - r*n1 r p q l s)^2 + ((p*p+q*q)*y - r*n2 r p q l s)^2
      = (p*p+q*q)^2 * (x*x + y*y - r*r)
        - 2*r*(p*p+q*q) * (n1 r p q l s * x + n2 r p q l s * y - r*(p*p+q*q))
        + r^2 * (n1 r p q l s ^ 2 + n2 r p q l s ^ 2 - (p*p+q*q)^2) := by
  unfold n1 n2; grind

/-- (3) 원과 직선의 공통점 X는 d²X = r·n 을 만족한다 (제곱합 = 0).
    ℝ에서는 제곱합 = 0 ⇒ 각 항 = 0 이므로 교점은 T = r·n/d² 하나뿐 → 접한다. -/
theorem unique_contact (r p q l s x y : α)
    (hl : l*l = p*p + q*q - r*r) (hs : s*s = 1)
    (hc : x*x + y*y = r*r)
    (hL : n1 r p q l s * x + n2 r p q l s * y = r*(p*p + q*q)) :
    ((p*p+q*q)*x - r*n1 r p q l s)^2 + ((p*p+q*q)*y - r*n2 r p q l s)^2 = 0 := by
  rw [key_identity, normal_sq r p q l s hl hs, hc, hL]; grind

/-- (4) 접점 T = r·n/d² 은 원 위에 있다: |r·n|² = r²·d⁴ -/
theorem contact_on_circle (r p q l s : α)
    (hl : l*l = p*p + q*q - r*r) (hs : s*s = 1) :
    (r*n1 r p q l s)^2 + (r*n2 r p q l s)^2 = r^2 * (p*p+q*q)^2 := by
  have h := normal_sq r p q l s hl hs
  grind

/-- (5) 접점 T = r·n/d² 은 직선 위에 있다: n·(r·n) = r·d²·d² -/
theorem contact_on_line (r p q l s : α)
    (hl : l*l = p*p + q*q - r*r) (hs : s*s = 1) :
    n1 r p q l s * (r*n1 r p q l s) + n2 r p q l s * (r*n2 r p q l s)
      = r*(p*p+q*q) * (p*p+q*q) := by
  have h := normal_sq r p q l s hl hs
  grind

/-- (6) 두 접선(s=1, s=-1)의 법선벡터 차이는 2l(−q, p). l ≠ 0이면 두 직선은 다르다. -/
theorem two_lines_differ_x (r p q l : α) :
    n1 r p q l 1 - n1 r p q l (-1) = -(2*l*q) := by
  unfold n1; grind
theorem two_lines_differ_y (r p q l : α) :
    n2 r p q l 1 - n2 r p q l (-1) = 2*l*p := by
  unfold n2; grind

/-! 수치 확인 (정수) -/
-- x²+y²=4, P(2,3): r=2, l=3, s=−1 → n=(13,0), 우변 26 → 13x=26 → x=2
example : n1 (2:Int) 2 3 3 (-1) = 13 ∧ n2 (2:Int) 2 3 3 (-1) = 0 := by decide
-- s=+1 → n=(−5,12) → −5x+12y=26
example : n1 (2:Int) 2 3 3 1 = -5 ∧ n2 (2:Int) 2 3 3 1 = 12 := by decide
-- |n|² = 169 = 13² = (p²+q²)²
example : (-5:Int)^2 + 12^2 = (2*2+3*3)^2 := by decide
