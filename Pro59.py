# python program to Sum of tuple elements

def summation(tuple1):
    test = list(tuple1)
    count =0
    for i in test :
        count+=i

    return count


str1 = input("Enter numbers with string: ")

tuple1 = tuple(int(item) for item in str1.split())
print("My tuple: ", tuple1) 

print("Sum of tuple elements is :  ",summation(tuple1))
