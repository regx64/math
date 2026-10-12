/-
  원 밖의 점에서 그은 접선 — 회전·복소수 형태 검증 (Lean 4 core, Mathlib 없음)
  원 x²+y²=r², 원 밖의 점 P(p,q), d²=p²+q², l²=d²−r², s²=1 (부호 ±)
  cos α = r/d, sin α = l/d  (가설로는 c·d = r, σ·d = l 로 넣음)
  모든 정리는 임의의 가환환 α에서 성립하므로 ℝ에서도 성립한다.
-/
open Lean.Grind

variable {α : Type} [CommRing α]

/-- d²·(접점)/r 에 해당하는 벡터 n = (rp − s·lq, rq + s·lp) -/
def n1 (r p q l s : α) : α := r*p - s*l*q
def n2 (r p q l s : α) : α := r*q + s*l*p

/-- |n|² = d⁴ -/
theorem normal_sq (r p q l s : α)
    (hl : l*l = p*p + q*q - r*r) (hs : s*s = 1) :
    n1 r p q l s ^ 2 + n2 r p q l s ^ 2 = (p*p + q*q)^2 := by
  unfold n1 n2; grind

/-! ## A. 회전 형태 -/

/-- P를 각 α (cos α = c, sin α = s·σ) 만큼 돌린 벡터 P' -/
def rot1 (c σ s p q : α) : α := c*p - s*σ*q
def rot2 (c σ s p q : α) : α := c*q + s*σ*p

/-- (A1) d·P' = n  (cos α = r/d, sin α = l/d) -/
theorem rot_scaled (r p q l s c σ d : α) (hc : c*d = r) (hσ : σ*d = l) :
    d * rot1 c σ s p q = n1 r p q l s ∧ d * rot2 c σ s p q = n2 r p q l s := by
  unfold rot1 rot2 n1 n2
  constructor <;> grind

/-- (A2) 회전해도 길이는 그대로: c²+σ²=1, s²=1 이면 |P'|² = |P|² -/
theorem rot_length (c σ s p q : α) (h : c*c + σ*σ = 1) (hs : s*s = 1) :
    rot1 c σ s p q ^ 2 + rot2 c σ s p q ^ 2 = p*p + q*q := by
  unfold rot1 rot2; grind

/-- (A3) 회전 형태 P'·X = r·d 에 d를 곱하면 성분 공식 n·X = r·d² 이 된다. -/
theorem rot_form_to_formula (r p q l s c σ d x y : α)
    (hc : c*d = r) (hσ : σ*d = l) (hd : d*d = p*p + q*q)
    (h : rot1 c σ s p q * x + rot2 c σ s p q * y = r*d) :
    r*(p*x + q*y) + s*l*(p*y - q*x) = r*(p*p + q*q) := by
  have e1 : d * rot1 c σ s p q = n1 r p q l s := (rot_scaled r p q l s c σ d hc hσ).1
  have e2 : d * rot2 c σ s p q = n2 r p q l s := (rot_scaled r p q l s c σ d hc hσ).2
  have key : n1 r p q l s * x + n2 r p q l s * y = d * (r*d) := by
    rw [← e1, ← e2, ← h]; grind
  unfold n1 n2 at key
  rw [hd.symm]; grind

/-- (A4) 주의: 극선 P·X = r² 을 O 중심으로 돌린 직선 P'·X = r² 은 원점과의 거리가 r²/d.
    접선(거리 r)이 되려면 우변이 r·d 여야 한다. 두 우변의 비: (r·d)/(r²) = d/r. -/
theorem polar_vs_tangent (r d : α) : r*d * r = r*r * d := by grind

/-! ## B. 복소수 형태  T = r(r + i·s·l) / P̄  ⇔  T·P̄ = r(r + i·s·l)
    T = r·n/d² 이므로 d²배 한 식 (r·n)·P̄ = r(r + i·s·l)·d² 를 성분별로 확인. -/

/-- (B1) 실수부: Re[(r·n)(p − qi)] = r·r·d² -/
theorem complex_re (r p q l s : α) :
    (r*n1 r p q l s)*p + (r*n2 r p q l s)*q = r*r*(p*p + q*q) := by
  unfold n1 n2; grind

/-- (B2) 허수부: Im[(r·n)(p − qi)] = r·(s·l)·d² -/
theorem complex_im (r p q l s : α) :
    (r*n2 r p q l s)*p - (r*n1 r p q l s)*q = r*(s*l)*(p*p + q*q) := by
  unfold n1 n2; grind

/-- (B3) 접점 T = r·n/d² 에서의 원 위의 접선 T·X = r² 을 d²/r 배 하면 공식과 같다. -/
theorem contact_tangent_is_formula (r p q l s x y : α) :
    n1 r p q l s * x + n2 r p q l s * y = r*(p*x + q*y) + s*l*(p*y - q*x) := by
  unfold n1 n2; grind

/-! ## 정수 수치 확인 -/
-- x²+y²=5, P(3,1): r=l=√5 → r·n = 5·(2,4)... 여기서는 √5 없이 T = (1,2), (2,−1) 을 직접 확인
-- T·P̄ = (1+2i)(3−i) = 5+5i = 5(1+i) = r(r+il)  (r=l=√5, r²=5)
example : (1:Int)*3 + 2*1 = 5 ∧ (2:Int)*3 - 1*1 = 5 := by decide
-- (2−i)(3−i) = 5−5i = r(r−il)
example : (2:Int)*3 + (-1)*1 = 5 ∧ (-1:Int)*3 - 2*1 = -5 := by decide
-- x²+y²=4, P(2,3): r=2, l=3, s=−1 → r·n = (26,0), d²=13 → T=(2,0)
example : 2 * n1 (2:Int) 2 3 3 (-1) = 26 ∧ 2 * n2 (2:Int) 2 3 3 (-1) = 0 := by decide
-- s=+1 → r·n = (−10,24) → T = (−10/13, 24/13)
example : 2 * n1 (2:Int) 2 3 3 1 = -10 ∧ 2 * n2 (2:Int) 2 3 3 1 = 24 := by decide
