# python progran to Convert List of Lists to Tuple of Tuples

list1 = [["hello","how","you"],["second","list","here"],["third","list","here"],["welcome"]]

print("\n\nOrginal list is : ", str(list1))

res = tuple(tuple(sub) for sub in list1)
print("the Converted data: ", str(res))