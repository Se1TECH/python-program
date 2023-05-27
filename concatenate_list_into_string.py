# Concatenate all elements in a list into a string

def conctenate1(list1):
    result = ''
    for element in list1:
        result += " "+ str(element)
    return result


list1 = [10,20,30,40,50]
print("String of list is: " ,conctenate1(list1))
