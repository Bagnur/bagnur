x=list(input().split())
y=0
for i in range(0, len(x)):
    p=int(x[i])
    if (p!=0):
        print(p, end=" ")
        y=y+1
for i in range(0, len(x)-y):
    print("0", end=" ")
