a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + delta**0.5)/(2*a)
    x2 = (-b - delta**0.5)/(2*a)
    print("Co 2 nghiem")
    print(x1, x2)
elif delta == 0:
    x = -b/(2*a)
    print("Nghiem kep")
    print(x)
else:
    print("Vo nghiem")