print("Hello and Welcome to the What Type of Sandwich Are You quiz!")

print("\n")  #this goes onto a new line

#we create variables so we can keep track of points
openFace_pts = 0

wrap_pts = 0

grilled_pts = 0

iceCream_pts = 0

hotDog_points = 0

#now we start

print("Question 1:")
print("Which of the following places would you want to live the most: New York City (a), Boston (b), Florida (c), Alaska (d)")
print("\n")

ans1 = input("Your answer: ")

if ans1 == "a":
  wrap_pts += 1

elif ans1 == "b":
  grilled_pts +=1

elif ans1 == "c":
  iceCream_pts += 1

elif ans1 == "d":
  hotDog_points += 1

else:
  print("Invalid Input, please answer a, b, c, or d")



if wrap_pts > grilled_pts and wrap_pts > iceCreamPts and wrap_pts > hotDog_points:
  print("Congratulations, you are a wrap!")
