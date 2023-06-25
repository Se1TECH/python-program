# Python code to demonstrate working of Word location in String 

import re

str1 = input("Enter Your String: ")
word = input("Enter Word for find index of it: ")

str1 = str1.split()
res = -1

for ind in str1:
    if len(re.findall(word, ind)) > 0:
        res = str1.index(ind)+1

print("The Location of word is: " + str(res))

