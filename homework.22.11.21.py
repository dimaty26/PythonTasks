def printSumOfNumberAndAmountOfNumbers(n, numbers):
  sum = 0

  if n > 100:
    print("Amount of numbers in list should be equal or less 100")
  elif n != len(numbers):
    print("Provided n does not match with numbers's length")
  else:
    for e in numbers:
      if not isinstance(e, int):
        print("Elements in list should be integers")
        break
      elif e > 500:
        print("Elements in list should be equal or less 500")
      if e % 7 == 0 and e % 3 == 0:
        sum += e
  if sum != 0:
    print(sum)
   