# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward
import room

# THIS PARAMETER CAN CHANGE!!!
# Make sure your code works for n_alcoves = 0, 1, 2, 3, and 4
# (You are allowed to use this parameter in your code)
n_alcoves = 3

# Draw the Level 5 version of the room
window = room.draw_room(level = 5, n_alcoves = n_alcoves)

###
# Start your code here

def R():
    right(90)

def L():
    left(90)

# def FA():
#     forward(40)
#     for i in range(3):
#         forward(40*2)
#         R()
#     for i in range(2):
#         L()
#         backward(40)
#     backward(80)
#     forward(40*4)
# FA()

forward(40*14)
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

 
# End your code here
###
 
window.exitonclick()