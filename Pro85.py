# python program to a basic student management system

class Student:
    def __init__(self,name, grade):
        self.name = name
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        self.students = []
    
    def add_student(self):
        name = input("Enter Student Name: ")
        grade = float(input("Enter Student Grade: "))
        student = Student(name, grade)
        self.students.append(student)
        print("Student Added Successfully")
    
    def display_students(self):
        if not self.students:
            print("\nNo Student Found")
        else:
            print("\n\n-----Student Information-----")
            for student in self.students:
                print(f"\nName:{student.name}\tGrade: {student.grade} ")

    def calculate_average_grade(self):
        if not self.students:
            print("\nNo Students Found")
        else:
            total_grades = sum(student.grade for student in self.students)
            average = total_grades/len(self.students)
            print(f"\nAverage Grade : {average:2f}")

sms = StudentManagementSystem()

while True:
    print("\n\n-----Student Management System-----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Calculate Average Grades")
    print("4. Exit")

    choice = input("Enter Your Choice(1-4): ")
    if choice == "1":
        sms.add_student()
    elif choice == "2":
        sms.display_students()
    elif choice == "3":
        sms.calculate_average_grade()
    elif choice == "4":  
        print("Exiting the Program.")
        break
    else:
        print("Invalid choice, Please try again")
        
