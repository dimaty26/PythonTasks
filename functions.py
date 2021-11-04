#function which prints greeting
def printText():
  print("Hi, Lida. How are you?")

#function which calculates square root
def sqrt(a):
    c = a / 2.0 
    while True:
        b = (c + a / c) / 2.0 
        if abs(c - b) < 0.00001: 
            return b
        c = b

#function which prints number
def printNumber(a):
  print(a)

def multiplyTwoNumbers(a, b):
  return a*b

def addTwoNumbers(a, b):
  return a+b

def subtractAfromB(a, b):
  return a-b

def division(a, b):
  return a / b

def raiseToThePower(a, b):
  return a**b