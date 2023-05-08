def display_stats(dict):
  for i in dict:
    print(i, "-", dict[i])


def choice():
  '''
  this function asks the user if they would like to: add a new bowler to the dictionary, remove a bowler from the ditionary, update a bowlers average

  returns the decision as a string
  '''

  c = input("Would you like to \"update\", \"add\", \"remove\": ")

  return c


def main():
  bowl_stats = {"Andrew": 162, "Jake": 172, "Spencer": 150, "Alek": 194}

  display_stats(bowl_stats)

  c = choice()
  
  if c == "update":
    
    '''
    ask the user for the bowler whose score they would like to update using input()
    update the value of that key
    '''

    key = input("Enter name of user to update: ")

    if key in bowl_stats.keys():
      val = input("Enter the new average for " + key  + ": ")
      bowl_stats.update({key:val})

    else:
      print("Cannot find user:", key)

  elif c == "add":
    '''
    here you should ask the user for a name and starting average using input(), 
    then add those values to the dictionary

    '''
    key = input("Enter name of user to add: ")
    val = input("Enter the average for " +  key  + ": ")
    bowl_stats.update({key:val})

    
  elif c == "remove":
    '''
    ask the user for the bowler they would like to remove
    remove them from the dictionary
    '''
    
    key = input("Enter the name of user to remove: ")
    if key in bowl_stats.keys():
      bowl_stats.pop(key)

    else:
      print("Cannot find user:", key)

  else:
    print("Invalid input...")
    

  print(bowl_stats) #this was to check my work
  

  

  


