import turtle
ANGLE = 90
def isPrime(number):
  
  for i in range (2,number):
    
    if number % i == 0:
      
      return False
    
  return True

def ulam_spiral(n):
    t = turtle.Turtle()
    wn= turtle.Screen()
    wn.bgcolor("black")
    t.speed(6)
    #t.penup()


    counter = 0
    for side_length in range(n):
      for f in range(side_length):
        counter += 1
        t.pencolor("white")
        if isPrime(counter):
          #t.pendown()
          t.pencolor("red")
          t.forward(1)
          print("PRIME" + str(counter))
          
        else:
          #t.penup()
          t.forward(1)
     
      t.left(ANGLE)

    return
  
  

  
  
