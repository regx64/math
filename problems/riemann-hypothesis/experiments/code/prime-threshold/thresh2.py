import numpy as np
exec(open("thresh.py").read().split("for a in")[0].replace('print("target','pass #'))
for M in [1500,3000]:
    lo,hi=3.0,3.5
    for _ in range(25):
        mid=(lo+hi)/2
        if lam_max(mid,M)>target: hi=mid
        else: lo=mid
    print("M=",M," a* (lambda_max(a*)=13.446) =",hi," e^{2a*}=",np.exp(2*hi), " lam(3.0)=",lam_max(3.0,M))
