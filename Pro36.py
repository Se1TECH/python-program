# Python program to find the sum
# and average of the list

list1 = [10,20,30,45,57,79]
sum = 0
for i in list1:
    sum += i

avg = sum/len(list1)
 
print("Sum : ", sum)
print("Average : ", avg)
