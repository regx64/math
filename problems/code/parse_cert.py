import re,sys,ast
txt=open('cert_matrix_q02_n333.pb.txt').read()
blocks=txt.split('constrained_tensors {')[1:]
out=[]
for b in blocks:
    m=re.search(r'constraints: "((?:[^"\\]|\\.)*)"',b)
    raw=ast.literal_eval('b"'+m.group(1)+'"') if m else b''
    vecs=[raw[i]|(raw[i+1]<<8) for i in range(0,len(raw),2)]
    lb=int(re.search(r'rank_lower_bound: (\d+)',b).group(1))
    out.append((vecs,lb))
with open('orbits.txt','w') as f:
    for v,lb in out: f.write(f"{lb} {len(v)} "+" ".join(map(str,v))+"\n")
from collections import Counter
print(len(out), Counter(len(v) for v,_ in out))
print([ (len(v),lb) for v,lb in out if len(v)<=2])
print("max lb",max(lb for _,lb in out))
