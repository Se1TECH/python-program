# python program to Sort Tuples by Maximum element

def get_max(sub1):
    return max(sub1)

tupleList = [(4,5,6,7),(19,10,4,5),(21,3,4,5),(1,2)]


print("The Orirgnal tuple list: ", str(tupleList))
tupleList.sort(key=get_max,reverse=True)

print("Sorted Tuples: ", str(tupleList))
