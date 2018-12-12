# If both password & username matched print - "Welcome Here"
# If Password incorrect print - "Incorrect Password. Try Again."
# If username incorrect print - "Incorrect Username"

username = "john007"
password = "321321"

given_username = input("Enter User Name Here: ")
given_pw = input("Enter Password Here: ")

if given_username == username:
  if given_pw == password:
    print("Welcome Here", given_username)
  else:
    print("Incorrect Password. Try Again.")
else:
  print("Incorrect User Name")

# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

import re

given_pw = input("Enter a Password Here: ")

if re.search('[a-z]', given_pw) is None:
  print("Password need at least 1 Lowercase")
elif re.search('[A-Z]', given_pw) is None:
  print("Password need at least 1 Uppercase")
elif re.search('[0-9]', given_pw) is None:
  print("Password need at least 1 number")
elif re.search('[$#@]', given_pw) is None:
  print("Password need at least 1 special character from '[$#@]'")
elif len(given_pw) < 6:
  print("Password length minium 6 character")
elif len(given_pw) > 16:
  print("Password length maximum 16 character")
else:
  print("Your Password looks strong..")

