#Dictionary in python

employee = {"Id":1,"Name":"John","Age":30,"Salary":10000}

for x in employee:
    print(x," : ",employee[x])

#add item in dictionary
print()
employee["Position"]  = "Manager"

for x in employee:
    print(x," : ",employee[x])
