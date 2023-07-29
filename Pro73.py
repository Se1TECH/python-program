# python program to Convert tuple to float
tuple1 = (9,87)

print("The Original tuple is: ", str(tuple1))
res = float('.'.join(str(ele) for ele in tuple1))
print("The float vlaue after conversion: ", str(res))