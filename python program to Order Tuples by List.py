#  python program to Order Tuples by List
tupleList1 = [("hello",4),("why",6),("xyz",8),("Python",2)]

print("The Oroginal list is: ", str(tupleList1))
list1 = ["Python","xyz","hello","why"]
temp = dict(tupleList1)
res = [(key, temp[key]) for key in list1]

print("The ordered list is: ", str(res))
