'''
    Lesson: Else
    Author: Jonisa Shanmuganantham
    Date Created: October 15, 2024
    Date Last Modified: October 15, 2024
'''

def q1(): 
  integer = int(input("Input an integer: "))
  if integer == 5:
    print("The number is Five")
  else:
    print("The number is not Five")

def q2(): 
  number = float(input("Input a number: "))
  if number > 0:
    print("Positive")
  else:
    print("Negative")

def q3(): 
  number = int(input("Input an integer: "))
  integer = number % 2
  if integer == 0:
    print("Even")
  else:
    print("Odd")

def q4(): 
  hello = input('Type "Hello": ')
  if hello == "Hello":
    print("The word is Hello")
  else:
    print("The word is not Hello") 


#Do not alter the following code
#Comment out the following code when running your tests

# q1()
# q2()
# q3()
# q4()
