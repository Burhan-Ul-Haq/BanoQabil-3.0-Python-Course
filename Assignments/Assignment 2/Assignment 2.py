# Task 01

class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name= first_name
        self.last_name= last_name
        self.age= age

    def displayinfo(self):
        print(f"\nFirst Name: {self.first_name}\nLast Name: {self.last_name}\nAge: {self.age:02d}")

person_first_name= input("\nTell Person First Name: ")
person_last_name= input("Tell Person Last Name: ")
person_age= int(input("Tell Person Age: "))

person= Person(person_first_name, person_last_name, person_age)
person.displayinfo()

# Task 02

class Student(Person):

    def __init__(self, first_name, last_name, age, student_id, Percentage):
        super().__init__(first_name, last_name, age)
        self.student_id= student_id
        self.Percentage= Percentage

    def displayinfo(self):
        super().displayinfo()
        print(f"Student ID: {self.student_id:02d}\nPercentage: {self.Percentage:02d}%")
    
student_first_name= input("\nTell Student First Name: ")
student_last_name= input("Tell Student Last Name: ")
student_age= int(input("Tell Student Age: "))
student_id= int(input("Tell Student ID: "))
student_percentage= int(input("Tell Student Percentage: "))

student= Student(student_first_name, student_last_name, student_age, student_id, student_percentage)
student.displayinfo()

# Task 03

class Teacher(Person):

    def __init__(self, first_name, last_name, age, teacher_id, salary):
        super().__init__(first_name, last_name, age)
        self.teacher_id= teacher_id
        self.salary= salary

    def displayinfo(self):
        super().displayinfo()
        print(f"Teacher ID: {self.teacher_id:02d}\nSalary: {self.salary}")

teacher_first_name= input("\nTell Teacher First Name: ")
teacher_last_name= input("Tell Teacher Last Name: ")
teacher_age= int(input("Tell Teacher Age: "))
teacher_id= int(input("Tell Teacher ID: "))
teacher_salary= int(input("Tell Teacher Salary: "))

teacher= Teacher(teacher_first_name, teacher_last_name, teacher_age, teacher_id, teacher_salary)
teacher.displayinfo()