# determines whether all are different from each other in python

def test(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False

print("Test of 1,4,6,7,8,9 : ",test([1,4,6,7,8,9]))
print("Test of 1,4,6,7,7,8,9 : ",test([1,4,6,7,7,8,9]))

        
