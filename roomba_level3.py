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

# Draw the Level 3 version of the room
window = room.draw_room(level = 3, radius = 5)

###
# Start your code here

forward(40*10)
backward(40*5)
left(90)
forward(40*5)
backward(40*10)
forward(40)
left(90)
forward(40*3)
left(180)
for i in range(4):
    forward(40*6)
    left(90)
    forward(40)
    left(90)
    forward(40*6)
    right(90)
    forward(40)
    right(90)
forward(40*6)
right(90)
forward(40)
left(90)
forward(40)
right(90)
forward(40*6)
right(90)
forward(40*8)
right(90)
forward(40*6)


# End your code here
###
 
window.exitonclick()