from random import randint

x = randint(0, 100)

if x <= 30:
    print("Rainy")
elif x <= 70:
    print("Cloudy")
else:
    print("Sunny")