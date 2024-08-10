Total_Marks= 0

Math= 0
Urdu= 0
Chemistry= 0
Physics= 0
Computer=0
Pakistan_Studies= 0
Islamiat= 0
English= 0

Math_Marks= int(input("Tell your Math Marks: "))
Urdu_Marks= int(input("Tell your Urdu Marks: "))
Chemistry_Marks= int(input("Tell your Chemistry Marks: "))
Physics_Marks= int(input("Tell your Physics Marks: "))
Computer_Marks= int(input("Tell your Computer Marks: "))
Pakistan_Studies_Marks= int(input("Tell your Pakistan_Studies Marks: "))
Islamiat_Marks= int(input("Tell your Islamiat Marks: "))
English_Marks= int(input("Tell your English Marks: "))

if Math_Marks > 0:
   Math += Math_Marks
if Urdu_Marks > 0:
   Urdu += Urdu_Marks
if Chemistry_Marks > 0:
   Chemistry += Chemistry_Marks
if Physics_Marks > 0:
   Physics += Physics_Marks
if Computer_Marks > 0:
   Computer += Computer_Marks
if Pakistan_Studies_Marks > 0:
   Pakistan_Studies += Pakistan_Studies_Marks
if Islamiat_Marks > 0:
   Islamiat += Islamiat_Marks
if English_Marks > 0:
   English += English_Marks

Total_Marks += Math
Total_Marks += Urdu
Total_Marks += Chemistry
Total_Marks += Physics
Total_Marks += Computer
Total_Marks += Pakistan_Studies
Total_Marks += Islamiat
Total_Marks += English

def grades(marks):
    if marks > 85:
        return("A")
    elif marks > 70:
        return("B")
    elif marks > 60:
        return("C")
    else:
        return("F")
    
Main= Total_Marks/800*100

print(f"Your Math Grade is {grades(Math)}")
print(f"Your Urdu Grade is {grades(Urdu)}")
print(f"Your Chemistry Grade is {grades(Chemistry)}")
print(f"Your Physics Grade is {grades(Physics)}")
print(f"Your Computer Grade is {grades(Computer)}")
print(f"Your Pakistan_Studies Grade is {grades(Pakistan_Studies)}")
print(f"Your Islamiat Grade is {grades(Islamiat)}")
print(f"Your English Grade is {grades(English)}")
print(f"Your Total Grade is {grades(Main)}")