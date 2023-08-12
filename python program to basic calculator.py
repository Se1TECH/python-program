# python program to basic calculator
def add(a,b):
    return a+b

def substraction(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b != 0:
        return a/b
    else: 
        return "Error : Cannot divide by zero" 

def calculator():
    print("Calculator")
    print("Operations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice: ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == "1":
        result = add(num1,num2)
        operator = "+"

    elif choice == "2":
        result = substraction(num1,num2)
        operator = "-"

    elif choice == "3":
        result = multiply(num1,num2)
        operator = "*"
    
    elif choice == "4":
        result = divide(num1,num2)
        operator = "+"
    
    else:
        print("Invalid choice")
    
    print(f"{num1} {operator} {num2} = {result} ")

#start the calculator
calculator()

    


