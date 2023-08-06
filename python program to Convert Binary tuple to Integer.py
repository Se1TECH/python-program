# python program to Convert Binary tuple to Integer

tuple1 = (1,0,1,1,0,1,1)
print("The Original tuple : " + str(tuple1))
res = int("".join(str(ele) for ele in tuple1 ),2)
print("The Decimal number is: " + str(res))
