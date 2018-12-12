#################################################################
                          # Problem 01
#################################################################
# Area of a Circle
from math import pi
r = float(input("Enter the Value of 'r': "))
area = pi * r ** 2
print("The Area is:", area)

#################################################################
                          # Problem 02
#################################################################
# If user input a vowel like a print - "a is Vowel"
# If user input a consonant like b print - "b is Consonant"
vowel = "aeiouAEIOU"
character = input("Enter a Character Here: ")

if character in vowel:
  print(character, "is Vowel")
else:
  print(character, "is Consonant")

#################################################################
                          # Problem 03
#################################################################
# If user input a fruit name with first letter in vowel print - "This is an apple"
# If user input a fruit name with first letter in consonant print - "This is a banana"
vowel = "aeiou"
fruit_name = input("Enter a Fruit Name Here: ")
fruit_name = fruit_name.lower()

if fruit_name[0] in vowel:
  print("This is an", fruit_name)
else:
  print("This is a", fruit_name)

#################################################################
                          # Problem 04
#################################################################
# User input a Mobile Number.
# Depending on first three digit it will show to user what operator it is
# If user input less than 11 digit it will show number is invalid 
# If user input more than 11 digit it will show number is invalid
# If user input something which is not in mobile operator it will show not available
mobile_number = input("Enter a Mobile Number Here: ")

if mobile_number[0:3] == "017":
  if len(mobile_number) != 11:
    print(mobile_number, "is invalid")
  else:
    print(mobile_number, "is Grameen Phone Operator")
elif mobile_number[0:3] == "018":
  if len(mobile_number) != 11:
    print(mobile_number, "is invalid")
  else:
    print(mobile_number, "is Aktel Operator")
elif mobile_number[0:3] == "016":
  if len(mobile_number) != 11:
    print(mobile_number, "is invalid")
  else:
    print(mobile_number, "is Airtel Operator")
elif mobile_number[0:3] == "019":
  if len(mobile_number) != 11:
    print(mobile_number, "is invalid")
  else:
    print(mobile_number, "is Banglalink Operator")
elif mobile_number[0:3] == "015":
  if len(mobile_number) != 11:
    print(mobile_number, "is invalid")
  else:
    print(mobile_number, "is Teletalk Operator")
else:
  print("Sorry, This Number is not Found in Databases...")



