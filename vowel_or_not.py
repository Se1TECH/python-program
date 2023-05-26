# Check entered character is vowel or not
def isVowels(charatcter):
    allVowels = "aeiou"
    return charatcter in allVowels

char1 = input("Enter Your Character: ")
print("Your charater is vowel : ", isVowels(char1))
