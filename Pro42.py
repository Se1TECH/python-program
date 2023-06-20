# Python3 code to count vowel in a string using set

def vowelCount(str1):
    count = 0
    vowel = set("aeiouAEIOU")
    for alphabet in str1:
        if alphabet in vowel:
            count = count + 1
    
    print("No of Vowels : ", count)

str1 = "Hello World How Are You"
vowelCount(str1)
        