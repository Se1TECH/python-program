# Python code to demonstrate Least Frequent Character in String
# naive method

str1 = input("Enter Your String: ")

print("Your Original String: ",str1)

all_freq = {}
for i in str1:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
res = min(all_freq, key = all_freq.get)

print("The Minimal of all character in string: ", str(res))

