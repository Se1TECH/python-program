# Least common multiple (LCM) of two positive integers in python
def lcm(x,y):
    if x > y:
        z = x
    else:
        z = y
    
    while(True):
        if(z%x == 0) and (z%y == 0):
            lcm = z
            break
        z += 1
    
    return lcm

print("LCM of 15,17 : " , lcm(15,17))
print("LCM of 10,15 : " , lcm(10,15))
print("LCM of 4,6 : " , lcm(4,6))
