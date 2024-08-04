Maths= 0
Chemistry= 0
Physics= 0
Computer= 0
English= 0

Maths_Marks= int(input("Tell the Maths Marks: "))
Chemistry_Marks= int(input("Tell the Chemistry Marks: "))
English_Marks= int(input("Tell the English Marks: "))
Computer_Marks= int(input("Tell the Computer Marks: "))
Physics_Marks= int(input("Tell the Physics Marks: "))

if Maths_Marks > 0:
    Maths += Maths_Marks

if Chemistry_Marks > 0:
    Chemistry += Chemistry_Marks

if English_Marks > 0:
    English += English_Marks

if Computer_Marks > 0:
    Computer += Computer_Marks

if Physics_Marks > 0:
    Physics += Physics_Marks

if [Computer, Physics, Chemistry, English, Maths] >60:
    print("F")

if [Computer, Physics, Chemistry, English, Maths] <70:
    print("C")

if [Computer, Physics, Chemistry, English, Maths] <80:
    print("B")

else:
    print("A")