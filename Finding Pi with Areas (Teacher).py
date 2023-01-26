import turtle

t = turtle.Turtle()

def circ_in_square(l):
  t.color("RED")
  t.begin_fill()
  #draws square
  t.forward(l/2)
  t.left(90)
  t.forward(l)
  t.left(90)
  t.forward(l)
  t.left(90)
  t.forward(l)
  t.left(90)
  t.forward(l/2)
  t.end_fill()

  t.color("BLUE")
  t.begin_fill()
  t.circle(l/2)  #draws circle
  t.end_fill()
  
  return



def circ_area(d):

  area = 3.14159265 * (d/2)**2
  
  return area


def square_area(s):

  area = s**2

  return area


def difference(area_1, area_2):

  diff = area_1 - area_2

  return diff
  

def area_ratio(area_1, area_2):

  ratio =  area_1/area_2

  return ratio




def find_pi():

  diameter = 100

  circ_in_square(diameter)

  blue = circ_area(diameter)

  square = square_area(diameter)

  red = difference(square, blue)

  pi = area_ratio(blue, red)

  print("The ratio of the circle's area to the square's area is:", pi)

  return pi
