#######################################################
                  # Problem 01
#######################################################
# If user input a number greater than 0 print - Positive Number
# If user input a number smaller than 0 like -1, -10, etc print - Negetive Number
# If user input 0 print - You enter zero

my_number = int(input("Enter a Number Here: "))

if my_number > 0:
  print(my_number, "is Positive")
elif my_number < 0:
  print(my_number, "is Negetive")
else:
  print("You Enter a Zero Right...")


#######################################################
                  # Problem 02
#######################################################
# User input any number like 1, 100, 10.89, etc
# If the number is able to divided by 2 like 10, 12, 20, etc print - Even Number
# If the number is not able to divided by 2 like 9, 13, 21, etc print - Odd Number

my_number = float(input("Enter a Number Here: "))

if my_number % 2 == 0:
  print(my_number, "is an Even Number")
else:
  print(my_number, "is an Odd Number")


######################################################
                  # Problem 03
######################################################
# User input any Alphabet he/ she like
# If input alphabet is uppercase like A print - A is Upper Case
# If input alphabet is lowercase like a print - a is Lower Case

my_alphabet = input("Enter Alphabet Here: ")

if my_alphabet >= 'a' and my_alphabet <= 'z':
  print(my_alphabet, "is Lower Case")
elif my_alphabet >= 'A' and my_alphabet <= 'Z':
  print(my_alphabet, "is Upper Case")
else:
  print("Nothing...")