x=int(input("Введите число:"))
y=int(input("Введите систему исчисления:"))
a=list(str(x))
print(a)
z=len(a)
print(z)
s=z-1
p=int
for i in range (z):
  p=p+(int(a[i]))*(y**s)
  print(p)
