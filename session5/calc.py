x = int(input("Nhap x: "))
y = int(input("Nhap y: "))
op = input("Operator: ")

result = 0
if op == "+":
    result = x + y
elif op == "-":
    result = x - y
elif op == "*":
    result = x * y
elif op == "/":
    result = x / y

print("{0} {1} {2} = {3}".format(x, op, y, result))