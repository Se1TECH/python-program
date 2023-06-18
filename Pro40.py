#Python program to capitalize first and last character of
# each word of a String

def cap(str1):
    s = str1
    return ' '.join(map(lambda s: s[:-1]+s[-1].upper(), s.title().split()))


str1 = input("Enter your string: ")
print("String Before use of cap function: ", str1)
print("String After use of cap function: ", cap(str1))


#Python program to capitalize first and last character of
# each word of a String

def cap(str1):
    s = str1
    return ' '.join(map(lambda s: s[:-1]+s[-1].upper(), s.title().split()))


str1 = input("Enter your string: ")
print("String Before use of cap function: ", str1)
print("String After use of cap function: ", cap(str1))


