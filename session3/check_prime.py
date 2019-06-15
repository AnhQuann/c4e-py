# n = int(input("Enter your number: "))
# i = 2
# is_prime = True
# while is_prime:
#     if n % i == 0:
#         is_prime = False
#     i += 1
# # Kết luận
# if is_prime == True:
#     print("LA SNT")
# else:
#     print("KHONG PHAI SNT")

# Cach 1:
n = int(input("Enter your number: "))
i = 2
is_prime = True
while i < n:
    if n % i == 0: # chia het hay khong?
        is_prime = False
    i += 1
if is_prime:
    print("LA SNT")
else:
    print("KHONG PHAI SNT")




# Cach 2:
n = int(input("Enter your number: "))
i = 2
loop = True
while loop:
    if n % i == 0: # chia het hay khong?
        loop = False
        print("Khong phai SNT")
    i += 1
    if i == n:
        loop = False
        print("SO NT")
