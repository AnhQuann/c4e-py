from turtle import *
speed(0)

length = 0

for i in range(500):
    forward(length)
    left(90)
    # length = length + 5
    length += 5

mainloop()