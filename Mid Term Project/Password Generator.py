import string

is_strong= True

print("Generate Password")

password= input("Tell your Password: ")

if len(password) < 8:
    print("Password must be longer than 8 for it to be called strong")
else:
    print("Checking Conditions...")
    is_strong= False
    
if not any(char.isdigit() for char in password):
    print("Password must have atleast one Digit")
    is_strong= False
    
if not any(char in string.punctuation for char in password):
    print("Password must contain atleast one Punctuation")
    is_strong= False

if not any(char == "_" for char in password):
    print("Password must contain atleast one '_'")
    is_strong= False

if is_strong:
    print("Your Password is Strong")
else:
     print(password)