x=list(input().split())
y=9999
for i in range(len(x)):
    k=int(x[i])
    if (k<y)and(k>0) :
        y=k
print(y)
