#---------------------Calculator----------------------------
from art import logo
from os import system

def add(n1, n2):
  """Adds 2 numbers"""
  return n1+n2

def substract(n1, n2):
  """Subtracts 2 numbers"""
  return n1-n2

def multiply(n1, n2):
  """Multiplies 2 numbers"""
  return n1*n2

def divide(n1 , n2):
   """Divides 2 numbers"""
   return n1/n2
  
operations = {
  "+": add,
  '-': substract,
  '*': multiply,
  "/": divide
}
print(logo)
def calculator():
  num1 = int(input("What is the first number?: "))
  num2 = int(input("What is the second number?: "))
  for symbol in operations:
    print(symbol)
  operation_symbol = input("Pick an operation from the value above ☝: ")
  calculation_function = operations[operation_symbol]
  first_answer = calculation_function(num1, num2)

  print(f"{num1} {operation_symbol} {num2} = {first_answer}")
  want_to_exit = input("Type 'y' to continue chaining or 'n' to exit:")
  if want_to_exit == 'y':
    pass
  else:
    print("Bye!")
    exit()
  while True:
    operation_symbol = input("Pick another operation: ")
    num3 = int(input("What is the next number?: "))
    calculation_function = operations[operation_symbol]
    second_answer = calculation_function(first_answer, num3)

    print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

    want_to_exit2 = input("Type 'y' to continue chaining or 'n' to start a new calculation:")
    if want_to_exit2 == 'y':
      first_answer=second_answer
    else:
      system('CLS')
      calculator()

calculator()