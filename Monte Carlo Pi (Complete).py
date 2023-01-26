import turtle
import random
import time

t = turtle.Turtle()


def circ_in_square(l):


  t.circle(l/2)
  t.forward(l/2)
  t.left(90)
  t.forward(l)
  t.left(90)
  t.forward(l)
  t.left(90)
  t.forward(l)
  t.left(90)
  t.forward(l/2)

  return




def random_dot(l):
  
  x = random.randint(-1*l/2, l/2)
  y = random.randint(0, l)
  
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.color("RED")
  t.dot(5)

  return [x, y]



def point_in_circ(point, d):

  x = point[0]
  y = point[1]/2

  if ((x*x) + (y*y)) < ((d/2)*(d/2)):

    return True

  else:
    False



  

def runner(n, l):

  in_circ = 0
  out_circ = 0
  t.speed(100)
  circ_in_square(l)
  t.hideturtle()
  for i in range(n):
    
    point = random_dot(l)
    
    if point_in_circ(point, l):
      in_circ += 1
      #print("IN:    ", point)

    else:
      out_circ += 1
      #print("OUT:    ", point)
    #time.sleep(2)
  print("Estimate of Pi:", in_circ/out_circ)

  return







runner(500, 250)
  



  



