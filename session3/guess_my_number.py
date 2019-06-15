from random import randint
n = randint(0, 100)

loop = True
while loop:
    player_number = int(input("Your number: "))
    if player_number < n:
        print("Qua nho")
    elif player_number > n:
        print("Qua to")
    else:
        print("Bingo")
        loop = False