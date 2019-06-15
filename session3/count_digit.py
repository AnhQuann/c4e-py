n = int(input("Enter your number: "))

# Cach 1:
count_digit = 0
loop = True
while loop:
    n = n // 10
    count_digit += 1
    if n == 0:
        loop = False
print(count_digit)

# Cach 2:
# while n > 0:
#     n = n // 10
#     count_digit += 1

# print(count_digit)

