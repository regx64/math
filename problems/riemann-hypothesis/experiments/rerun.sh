#!/bin/sh
# Re-run archived RH experiment scripts in throw-away copies of their directories.
# Usage (from repo root):  sh problems/riemann-hypothesis/experiments/rerun.sh LANE OUTDIR
# Each line of a lane is "dir script timeout_seconds [args]". Side files written by a script
# (zeros.pkl, a.pkl, ...) land in the temporary copy, never in experiments/code/.
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
LANE=$1; OUT=$2; mkdir -p "$OUT"
LOG="$OUT/log-$LANE.tsv"; printf "dir\tscript\texit\tseconds\n" > "$LOG"
WORK=$(mktemp -d)
case $LANE in
  A) LIST="weil-identity zeros.py 900
weil-identity weil.py 900
weil-identity weil2.py 900
weil-identity checks.py 900
prime-threshold thresh.py 900
prime-threshold thresh2.py 1800
landau-lp lp.py 900
resolution-barrier resolution.py 300
hybrid-moments hybrid.py 300
ground-state constants.py 300
ac-round5-slack slack.py 300
ac-round5-slack slack2.py 900
ac-round5-slack slack4.py 900
ac-round5-slack slack5.py 900
ac-round5-slack slack3.py 1200
ac-round5-slack slack6.py 1200" ;;
  B) LIST="ac-audit e1_singlepair.py 900
ac-audit e1b.py 900
ac-audit e2_lattice.py 1200
ac-audit e2b.py 1200
ac-audit e4_mixed.py 900
ac-audit e4b.py 900
ac-audit e4c_exact.py 900
ac-audit e5b.py 900
ac-audit e6_check.py 1800
ac-audit e5_adv.py 1800 2
ac-audit e3_segments.py 2400" ;;
  C) LIST="jensen-interlacing coeffs.py 3600
jensen-interlacing test.py 3600
jensen-interlacing ce.py 900
jensen-interlacing ce2.py 900
jensen-interlacing ce_exact.py 900" ;;
esac
echo "$LIST" | while read d s t args; do
  [ -d "$WORK/$d" ] || cp -r "$HERE/code/$d" "$WORK/$d"
  start=$(date +%s)
  ( cd "$WORK/$d" && timeout "$t" python3 "$s" $args ) > "$OUT/$d--$s.out" 2>&1
  rc=$?; end=$(date +%s)
  printf "%s\t%s\t%s\t%s\n" "$d" "$s" "$rc" "$((end-start))" >> "$LOG"
done
cp "$WORK/weil-identity/zeros.pkl" "$OUT/zeros.regenerated.pkl" 2>/dev/null || true
cp "$WORK/jensen-interlacing/a.pkl" "$OUT/jensen-a.regenerated.pkl" 2>/dev/null || true
echo done > "$OUT/DONE-$LANE"
