def mod_test():

  x = input("Enter a number: ")
  
  y = input("Enter a number to divide x by: ")
  
  x = int(x)  #turn x into an integer
  
  y = int(y)  #turn y into an integer
  
  mod = x % y
  
  print(x,"%",y,"=", mod)

  return



def isPrime(num):

  for i in range(2, num):
  
    if num % i == 0:
  
      return False

  return True


