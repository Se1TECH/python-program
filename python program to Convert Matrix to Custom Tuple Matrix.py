#pyhton program to Convert Matrix to Custom Tuple Matrix

list1 = [[4,5,6],[7,8,9],[1,2,3],[3,5,6],[6,9,2]]

print("The Orginal list 1: ", str(list1))

addToList = ['hello','welcome','to','my','video']

res =[]

for idx ,ele in zip(addToList,list1):
    for e in ele:
        res.append((idx,e))


print("Matrix after conversion: ", str(res))
