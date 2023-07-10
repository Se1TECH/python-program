#python Remove substring list from String

str1 = "Hello World How are you?"
print("original string: ", str1)

list1 = ["How","you"]

for sub in list1:
    str1 = str1.replace(' '+sub+' ',' ') 

print("The string after substring removal: ",str1)
