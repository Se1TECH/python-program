# find common elements in three sorted arrays
from collections import Counter
def commonElement(ar1,ar2,ar3):
    ar1 =  Counter(ar1)
    ar2 =  Counter(ar2)
    ar3 =  Counter(ar3)

    resultDict = dict(ar1.items() & ar2.items() & ar3.items())
    common = []

    for (key,val) in resultDict.items():
        for i in range(0,val):
            common.append(key)
    
    print(common)

if __name__ == "__main__":
    ar1 = [1,2,3,4,5,6,7,9]
    ar2 = [5,6,7,8,9,0]
    ar3 =[6,7,3,8,9]
    commonElement(ar1, ar2, ar3)
