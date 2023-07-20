# Python program to find tuples which have all
# elements divisible by K from a list of tuples

list1 = [(6,24,12),(7,9,6),(3,9,27)]

print("The Original list : ", str(list1))
k=3

res = [sub for sub in list1 if all(ele % k == 0 for ele in sub)]

print("k multiply element tuples: ", str(res))




