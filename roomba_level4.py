# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(15)

# Draw the Level 4 version of the room
window = room.draw_room(level = 4, n_alcoves = 1, radius = 5)

###
# Start your code here

def R():
    right(90)

def L():
    left(90)

forward(40*10)
backward(40*5)
L()
forward(40*9)
backward(40*14)
forward(40)
L()
forward(40*3)
left(180)
for i in range(4):
    forward(40*6)
    L()
    forward(40)
    L()
    forward(40*6)
    R()
    forward(40)
    R()
forward(40*6)
R()
forward(40)
L()
forward(40)
R()
forward(40*6)
R()
forward(40*8)
R()
forward(40*6)
R()
forward(40*4)
L()
forward(40*3)
L()
forward(40)
R()
for i in range(3):
    forward(40*2)
    R()
for i in range(2):
    L()
    backward(40)
backward(80)
forward(40*4)

# End your code here
###
 
window.exitonclick()