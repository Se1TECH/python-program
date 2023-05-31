# Sort three integers without using conditional statements and loops in python
n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))
n3 = int(input("Enter Third Number: "))

s1 = min(n1,n2,n3)
s3 = max(n1,n2,n3)
s2 = (n1+n2+n3) - s1 -s3

print("Sorted Integers: ",s1,s2,s3)

