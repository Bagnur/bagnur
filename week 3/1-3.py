x=set(input().split())
y=set(input().split())
z=x.intersection(y)
for i in z:
    print(i, end=" ")