def check_mod_11(num_string):

  #get the batch of numbers, remember we are dealing with a string
  batch1 = num_string[0:-1:2]
  batch2 = num_string[1:-1:2]

  sum1 = 0
  sum2 = 0

  #sum the first batch
  for char in batch1:
    i = int(char)

    sum1 += i

  #sum the second batch
  for char in batch2:
    i = int(char)

    sum2 += i

  #multiply sum1 by 3
  prod1 = sum1 * 3

  total_sum = prod1 + sum2

  #mod by 10
  remainder = total_sum % 10

  check_digit = 10 - remainder

  

  if check_digit == int(num_string[-1]):
      return True

  else:
      
      return False
    
  
