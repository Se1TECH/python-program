#Python program to Replace Different characters in String at Once
str1 = input("Enter your string: ")
print("The Original string is: " , str1)

map_dic = {'H':'1','e':'4','w':'6'}

res = ''.join(idx if idx not in map_dic else map_dic[idx] for idx in str1)

print("The Converted String : ", str(res))
