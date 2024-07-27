# Name: Burhan Ul Haq
# Roll No.: 8
# Email: burhanrgrg8@gmail.com

# Name: Hanzala Rashid
# Roll No.: 15
# Email: hanzalarashid7@gmail.com

                                                                                                        # Password Strength Checker

"""This is a Password Strength Checker, 
Sometimes there a need of checking that if your Password is strong, so this program helps to do it with helps of its conditions which checks if user entered passwords contains all the coditions
 if not the user is prompted by 'Your Password isn't strong enough' """

import string

print("Generate Password")

# This prompts the User to enter desired Password
password= input("Tell your Password: ")

# This variable checks the conditions of the password whether it is True or not and by default it is True as Conditions checks that if not the password has the conditions
is_strong = True

# These are the conditions the input password goes through for it to be considered strong

# This Condition checks that the password entered is at least 8 characters long

if len(password) < 8:
    print("Password must be longer than 8 for it to be called strong")
    is_strong= False
else:
    print("Checking Conditions...")

# This Condition checks that the password entered has Upper Case Letter or not
if not any(char in string.ascii_uppercase for char in password):
     print("Password must contain atleast one Upper Case Letter")
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
if is_strong:
        print(f"Your Password is Strong, Your Password is: {password}")
else:
     print(f"Your Password isn't strong enough, Your Password is: {password}")