#Введите с клавиатуры 5 положительных целых чисел. Вычислите сумму #тех из них, которые делятся на 4 и при этом заканчиваются на 6. #Программа должна вывести одно число: сумму чисел, введенных с #клавиатуры, кратных 4 и оканчивающихся на 6.

#Tests: 
# input: 9 3 76 94 -4 output: error
# input: 12 16 26 36 30 output: 52

def sumNumbersDivisedByFour():
  s1 = input("first number: ")
  s2 = input("second number: ")
  s3 = input("third number: ")
  s4 = input("fourth number: ")
  s5 = input("fifth number: ")

  nums = [s1, s2, s3, s4, s5]
  sum = 0

  for element in nums:
    if int(element) < 0:
      print("error")
      break
    else:
      if int(element[len(element) - 1]) == 6 and int(element) % 4 == 0:
        sum += int(element)

  if sum != 0:
    print(sum)