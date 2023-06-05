# Display numbers divisible by 5 from a list in python

list1 = [10,20,11,1,6,8,9,40,50,7]

print("Given list : ",list1)
print("Divisible 5 : ")

for num in list1:
    if num % 5 ==0:
        print(num)
