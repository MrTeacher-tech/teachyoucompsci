import csv

def display_stats(dict):
  for i in dict:
    print(i, "-", dict[i])


def choice():
  '''
  this function asks the user if they would like to: add a new bowler to the dictionary, remove a bowler from the ditionary, update a bowlers average

  returns the decision as a string
  '''

  c = input("Would you like to \"update\", \"add\", \"remove\", \"exit\": ")

  return c


def get_stats():

  '''
  this function should read stats.csv and turn it into a dictionary

  return the dictionary
  '''

  #this is copy and pasted from Writing to files challenge set
  input_file = csv.reader(open("stats.csv"))
  myDict = {}
  for row in input_file:
    key = row[0]
    val = row[1]

    myDict.update({key:val})

  return myDict

def main():
  bowl_stats = get_stats()

  while True:
    print("\n")
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
  
    
    elif c == "exit":
      with open('stats.csv', 'w', newline='') as csvfile:
        statwriter = csv.writer(csvfile)
        
        for key in bowl_stats:
          line = [key , bowl_stats[key]]
          statwriter.writerow(line)
    
      break 
        
    
    else:
      print("Invalid input...")
    

  
#run the program
main()
  

  


