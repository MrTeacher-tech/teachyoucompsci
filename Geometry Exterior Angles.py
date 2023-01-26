import turtle
turtle = turtle.Turtle()
t = turtle

t.speed(1)

NUM_SIDES = 4

EXTERIOR_ANGLE = 90

SIDE_LENGTH = 50

for i in range(NUM_SIDES):

  t.forward(SIDE_LENGTH)
  t.left(EXTERIOR_ANGLE)




