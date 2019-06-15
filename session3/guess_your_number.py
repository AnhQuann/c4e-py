print('''
Guess your number game
Now think of a number from 0 to 100, then press 'Enter'
All you have to do is to answer to my guess
'c' if my guess is 'C'orrect
's' if my guess is 'C'orrect
'l' if my guess is 'C'orrect
''')

low = 0
high = 100

loop = True

while loop:
    mid = (low + high) // 2
    answer = input("Is {} your number? ".format(mid))

    if answer == 'c':
        print("Bingo")
        loop = False
    elif answer == 'l':
        high = mid
    elif answer == 's':
        low = mid