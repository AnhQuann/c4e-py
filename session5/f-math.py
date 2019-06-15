from random import randint, choice
from functions.calculate import calc


x = randint(0, 9)
y = randint(0, 9)
list_op = ["+", "-", "*", "/"]
op = choice(list_op)

result = calc(x, y, op)

error = choice([-1, 0, 0, 0, 0, 0, 1])
display_result = result + error

print("{0} {1} {2} = {3}".format(x, op, y, display_result))
answer_input = input("(Y/N)? ").lower()

if answer_input == "y":
    if error == 0:
        print("Hura!")
    else:
        print("Wrong!")

elif answer_input == "n":
    if error == 0:
        print("Wrong!")
    else:
        print("Hura!")