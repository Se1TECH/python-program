#python program to Remove K length Duplicates from String

str1 = input("Enter your String: ")

print("Your Original String: ", str1)

k = int(input("Enter Your kth number: "))

memo = set()
res = []
for idx in range(0,len(str1) - k):
    sub = str1[idx:idx+k]
    if sub not in memo:
        memo.add(sub)
        res.append(sub)

res = ''.join(res[ele] for ele in range(0,len(res),k))

print("The modified string: ", str(res))