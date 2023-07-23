# python program to Convert Tuple Matrix to Tuple List
tupleList = [[(1,2),(3,4)],[(5,6),(7,8)],[(9,10),(11,12)]]

print("Orginal list is: ", str(tupleList))

temp =  [ele for sub in tupleList for ele in sub]

res = list(zip(*temp))

print("The Coverted Tuple List :  ", str(res))