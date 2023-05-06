# el if in Python
# Que: Find the maximum number out of three numbers
num1 = int(input("Enter Num 1: "));
num2 = int(input("Enter Num 2: "));
num3 = int(input("Enter Num 3: "));

if num1 > num2  and  num1 > num3 :
    print("Num1 is Maximum");  
elif num2 > num1 and  num2 > num3 :
    print("Num2 is Maximum");  
else:
    print("Num3 is MAximum Number");
