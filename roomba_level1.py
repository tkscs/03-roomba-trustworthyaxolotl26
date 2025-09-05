# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Ellie
# -----------------------------------------------------------------------------
 
from turtle import left, forward, backward
#from turtle import right
import room

# Draw the Level 1 version of the room
window = room.draw_room(level = 1)

###
# Start your code here

for i in range(2):
    forward(40*4)
    left(90)
    forward(40)
    left(90)
    forward(40*4)
    left(270)
    forward(40)
    left(270)
forward(40*4)

# End your code here
###
 
window.exitonclick()