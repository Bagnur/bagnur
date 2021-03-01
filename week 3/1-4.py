x=list(input().split())
x1=int(x[0])
x2=int(x[1])
y=set()
z=set()
for i in range(0, x1):
    y1=int(input())
    y.add(y1)
for i in range(0, x2):
    z1=int(input())
    z.add(z1)
u=y.intersection(z)
print(len(u))
for i in u:
    print(i, end=" ")
print(" ")

d=y.difference(z)

print(len(d))
for i in d:
    print(i, end=" ")
print(" ")
s=z.difference(y)
print(len(s))
for i in s:
    print(i, end=" ")