from calculatorart import logo
print(logo)
def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
  return a/b
def mod(a,b):
  return a%b
def power(a,b):
  return a**b
num1=int(input("Enter your first operand "))
end=False 
while not end  :
  operator=input("Enter the operator : +,-,*,/,%,^")
  num2=int(input("Enter your second operand "))
  if operator=='+' :
    answer=(add(num1,num2))
  elif operator=='-' :
    answer=(sub(num1,num2))
  elif operator=='*' :
    answer=(multiply(num1,num2))
  elif operator=='/' :
    answer=(divide(num1,num2))
  elif operator=='%' :
    answer=(mod(num1,num2))
  elif operator=='^' :
    answer=(power(num1,num2))
  else :
    print("Wrong input given")
  print ( f"Answer : {answer} \n"  )
  choice= (input("Do you want to continue ? - Enter y or n for yes or no respectively "+"\n")).lower()
  if choice =="y": 
    end = False 
  else:
    
    end =True 
  continue_with_same=(input("would you like to use the answer as the operand again - Enter y for yes or n for no  ? " +"\n")).lower()
  if continue_with_same=="y":
    num1= answer
  else :
    num1=int(input("Enter your first operand "))
