import mpmath, pickle, time
mpmath.mp.dps=20
t=time.time(); Z=[]
n=1
while True:
    z=float(mpmath.zetazero(n).imag); Z.append(z); n+=1
    if z>700: break
pickle.dump(Z,open("zeros.pkl","wb"))
print(len(Z), Z[-1], time.time()-t)
