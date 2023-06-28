# Python code to demonstrate working of Sort String list by K character frequency
list1 =["Hello","How","are","you"]

print("The Original list is : ", str(list1))

k='r'
res= sorted(list1,key = lambda ele:-ele.count(k))
print("Sorted String:  ", str(res))
