#pyhton program Find all duplicate characters in string

def duplicate(string1):
    chars ={}

    for char in string1:

        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    
    duplicates = []

    for char, count in chars.items():
        if count > 1:
            duplicates.append(char)

    return duplicates


str1 = input("Enter Your String: ")
print("Duplicate character list: ", duplicate(str1))