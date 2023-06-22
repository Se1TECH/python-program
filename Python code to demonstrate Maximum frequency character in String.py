# Python code to demonstrate Maximum frequency character in String
# naive method

str1 = input("Enter Your String: ")

print("Your Orginal String is: ", str1)

all_freq = {}

for i in str1:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
    
res = max(all_freq,key=all_freq.get)


print("Your Most frequent character is:  ", str(res)) 
