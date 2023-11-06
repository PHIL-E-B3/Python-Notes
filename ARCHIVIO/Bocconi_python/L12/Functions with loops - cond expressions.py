
def sum_range(num):
  total = 0
  for n in range(1,num+1):
    total = total + n
  return total

  
def discount(quant, price):
  if quant > 100:
    total = quant * price * (1 - 0.4)
  elif quant > 50:
    total = quant * price * (1 - 0.2)    
  else:
    total = quant * price
  return total  


def odd_even(num):
  count_odd = 0
  count_even = 0
  for n in range(1,num+1):
    if n % 2 == 0:
      count_even = count_even + 1
    else:
      count_odd = count_odd + 1
  print("Number of even numbers :",count_even)
  print("Number of odd numbers :",count_odd)
  return count_even
