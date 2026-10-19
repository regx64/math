import numpy as np
from acmodel import *
print("E1b. I1 check: sum_k v_z(k)^2 -> 1 and sum |v|^2 -> S as grid grows (indicator exact sinc)")
win=Window("indicator")
for D in [0.25,1.0,2.0]:
    for K in [100,10000,1000000]:
        k=np.arange(-K,K+1); v=v_exact_indicator([0.3-1j*D],k)[0]
        print(f" D={D} grid=±{K}: sum v^2={ (v**2).sum().real:.8f}{(v**2).sum().imag:+.1e}i   sum|v|^2={(np.abs(v)**2).sum():.4f}  (S={win.S(D):.4f})")
win=Window("taper0.1")
for D in [0.25,1.0]:
    k=np.arange(-300,301); v=I1_vectors2(win,[0.3-1j*D],k)[0]
    print(f" taper0.1 D={D} grid=±300: sum v^2={(v**2).sum().real:.6f}{(v**2).sum().imag:+.1e}i  sum|v|^2={(np.abs(v)**2).sum():.4f} (S={win.S(D):.4f})")
