# Name: Burhan Ul Haq
# Roll No.: 8
# Email: burhanrgrg8@gmail.com

                                                                                                        # Password Strength Checker

"""This is a Password Strength Checker, 
Sometimes there a need of checking that if your Password is strong so this program helps to go it with helps of its conditions which checks if user entered passwords contains all the coditions
 if not the user is prompted by 'Your Password isn't strong enough' """

import string

# This variable checks the conditions of the password whether it is True or not and by default it is True as Conditions checks that if not the password has the conditions
is_strong= True

print("Generate Password")

# This prompts the User to enter desired Password
password= input("Tell your Password: ")

# These are the conditions the input password goes through for it to be considered strong

# This Condition checks that the password entered is at least 8 characters long

if len(password) < 8:
    print("Password must be longer than 8 for it to be called strong")
else:
    print("Checking Conditions...")
    is_strong= False

# This Condition checks that the password entered has Digits or not
if not any(char.isdigit() for char in password):
    print("Password must have atleast one Digit")
    is_strong= False

# This Condition checks that the password entered has Punctuations or not
if not any(char in string.punctuation for char in password):
    print("Password must contain atleast one Punctuation")
    is_strong= False

# This Condition checks that the password entered has a '_' or not
if not any(char == "_" for char in password):
    print("Password must contain atleast one '_'")
    is_strong= False

# If all the Conditions are True the User is prompted by your password is strong
if is_strong is False:
        print("Your Password is Strong")
else:
     print(f"Your Password isn't strong enough, Your Password is: {password}")