# Python program to remove even
# elements from a list 

list1 = [10,20,12,13,15,17,19,30]

for ele in list1:
    if ele%2 == 0:
        list1.remove(ele)

print("new List after removing all even elements from the list: ", list1)
