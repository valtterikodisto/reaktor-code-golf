v=input
q,g,m,w=int(v()),v(),0,""
x=len(g)
for i in range(x):
 if i+q<x:j=g[i:i+q]
 e=eval("*".join(j))
 if e>m:m,w=e,"".join(j)
print(j)