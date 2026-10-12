#!/bin/sh
# Markdown 노트를 LaTeX 조각(latex/gen/)으로 변환한다. 저장소 루트에서 실행: sh latex/md2tex.sh
set -e
conv() { pandoc -f markdown -t latex --top-level-division=section "$1" | python3 -c '
import re,sys
s=sys.stdin.read()
s=re.sub(r"\\hypertarget\{[^}]*\}\{%\n(\\(?:sub)*section\{.*?\})\\label\{[^}]*\}\}",lambda m:m.group(1).replace("\n"," "),s,flags=re.S)
if len(sys.argv)>1: s=s.replace("\\section{","\\subsection{")
sys.stdout.write(s)' $2 > "$3"; }
tmp=$(mktemp -d)
awk '/^## 외심 빠르게 구하기/{f=1} f' learning/analytic-geometry.md | sed 's/^## /# /' > $tmp/geo.md
awk '/^## 응용: 페이지랭크/{f=1} /^## 다음/{f=0} f' learning/linear-algebra.md | sed 's/^## /# /' > $tmp/la.md
conv $tmp/geo.md sub latex/gen/geometry-extra.tex
conv $tmp/la.md sub latex/gen/linear-algebra-extra.tex
for f in discrete-math combinatorics exponents shapley-value hilbert-problems lean; do conv learning/$f.md "" latex/gen/$f.tex; done
for f in matrix-mult-3x3 original-problems candidates; do conv problems/$f.md "" latex/gen/$f.tex; done
for f in algebra-graduate algebra-undergraduate geometry-discussion; do conv problem-sets/$f.md "" latex/gen/$f.tex; done
sed -i '1s/.*/\\section{\\texorpdfstring{\\(3\\times3\\) 행렬곱의 rank (\\(\\mathbb F_2\\))}{3×3 행렬곱의 rank (F2)}}/' latex/gen/matrix-mult-3x3.tex
rm -rf $tmp
