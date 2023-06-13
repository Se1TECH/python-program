# Python code to count the number of occurrences

def countEle(list1,search):
    count =0
    for ele in list1:
        if(ele == search):
            count = count+1
    return count


list1 = [10,20,30,40,10,20,20,20,20,30,10]
search = 20

print('{} has occured {} Times'.format(search,countEle(list1,search)))