import numpy as np
exec(open("weil.py").read().split("for a,om in")[0])
for M in [3001,12001]:
    zs,rhs,*_=check(1.2,30.0,M=M); print(M, zs-rhs)
    zs,rhs,*_=check(1.6,0.0,M=M); print(M, zs-rhs)
