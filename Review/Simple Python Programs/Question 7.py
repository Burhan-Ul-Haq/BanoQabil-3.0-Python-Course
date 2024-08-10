Total_Subjects= int(input("Tell the Total Number Of Subjects: "))

Subjects_Names= []
for i in range(Total_Subjects):
    Subjects_Name= (input("Tell the Name of the Subject: "))
    Subjects_Names.append(Subjects_Name)

Subjects= {}
for Subject in Subjects_Names:
    Marks= int(input(f"Tell your {Subject} Marks: "))
    Subjects[Subject] = Marks

def grades(marks):
    if marks >= 85:
        return("A")
    elif marks >= 70:
        return("B")
    elif marks >= 60:
        return("C")
    else:
        return("F")
print("Calculating Grades...")
for Subject, Marks in Subjects.items():
    print(f"Your {Subject} Grade is: {grades(Marks)}")

Total_Marks= 0
Total_Marks += sum(Subjects.values())

Max_Marks= Total_Subjects*100
Main= Total_Marks/Max_Marks*100
print(f"Your Total Grade is: {grades(Main)}")