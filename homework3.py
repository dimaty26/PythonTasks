#Homework
#Введите с клавиатуры 8 положительных целых чисел. Определите, сколько из них делятся на 3 и при этом заканчиваются на 4. Программа должна вывести одно число: количество чисел, кратных 3 и оканчивающихся на 4.

def countingNumbers():
  s1 = input("first number: ")
  s2 = input("second number: ")
  s3 = input("third number: ")
  s4 = input("fourth number: ")
  s5 = input("fifth number: ")
  s6 = input("sixth number: ")
  s7 = input("seventh number: ")
  s8 = input("eighth number: ")

  nums = [s1, s2, s3, s4, s5, s6, s7, s8]
  sum = 0

  for element in nums:
    if int(element) < 0:
      print("error")
      break
    else:
      if int(element[len(element) - 1]) == 4 and int(element) % 3 == 0:
        sum += 1

  if sum != 0:
    print(sum)