# code to demonstrate working of Convert numeric words to numbers
# Using join() + split()

dict1 = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
    'zero':'0',
}

str1 = input("Enter Your Numeric words : ")
print("Original String: ", str1)

res = ''.join(dict1[ele] for ele in str1.split())

print("The String After Performing: ", res)
