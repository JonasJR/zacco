import math

x = 0
y = 0

print "Give instructions in the form of [direction steps] and finnish with a blank input"
while True:
    tpl = raw_input("Please enter direction: ")
    if not tpl:
        break
    d, steps = tpl.split(" ")
    if d == "UP":
        x += int(steps)
    elif d == "DOWN":
        x -= int(steps)
    elif d == "RIGHT":
        y += int(steps)
    elif d == "LEFT":
        y -= int(steps)
print abs(x) + abs(y)
