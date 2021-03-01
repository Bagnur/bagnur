x=int(input())
d={}
for i in range(0, x):
    x=input().split()
    d[x[0]]=x[1]
    d[x[1]]=x[0]
z=input()
print(d[z])
