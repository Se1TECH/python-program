#  Convert feet and inches to centimeters in python

h_feet = int(input("Enter Feet: "))
h_inch = int(input("Enter Inch: "))

h_inch += h_feet*12
h_cm = round(h_inch *  2.54,1)
print("Your Height is in cm: ", h_cm)