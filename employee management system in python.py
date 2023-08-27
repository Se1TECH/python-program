# employee management system in python

class Employee:
    def __init__(self,emp_id,name,position):
        self.emp_id =emp_id
        self.name = name
        self.position = position
    
class EmployeeManager:
    def __init__(self):
        self.employees = []
    
    def add_employee(self,employee):
        self.employees.append(employee)
        print("Employee added Successfully.")
    
    def view_employee(self):
        if not self.employees:
            print("No Employees Found.")
        else:
            print("\n--- Employees ---")
            for index,employee in enumerate(self.employees,start=1):
                print(f"{index}. Employee Id: {employee.emp_id}, Name: {employee.name}, Position: {employee.position}")
        
    def search_employee(self,search_term):
        matching_employees = []
        for employee in self.employees:
            if search_term.lower() in employee.name.lower() or search_term.lower() in employee.position.lower():
                matching_employees.append(employee)
    
        if not matching_employees:
            print("Print No matching Employees found.")
        else:
            print("\n----- Matching Employees -----")
            for index,employee in enumerate(matching_employees,start=1):
                print(f"{index}. Employee Id: {employee.emp_id}, Name: {employee.name}, Position: {employee.position}")
    
#create Employee manager
emp_manager = EmployeeManager()

#menuLoop

while True:
    print("\n----- Employee Management System -----")
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Search Employee")
    print("4. Exit")

    choice = input("Enter Your choice: ")
    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        position = input("Enter Employee Position: ")
        employee = Employee(emp_id,name,position)
        emp_manager.add_employee(employee)
    
    elif choice == "2":
        emp_manager.view_employee()
    
    elif choice == "3":
        search_term = input("Enter Search Term: ") 
        emp_manager.search_employee(search_term)
    
    elif choice == "4":
        print("Exiting from Employee Management System.")
        break

    else:
        print("Invalid Choice. Please Try Again.")





