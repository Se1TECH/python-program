#create calendar forb user entered month and year in python.
import calendar
year =  int(input("Enter Year of Calendar: ")) 
month =  int(input("Enter Month of Calendar: ")) 

print(calendar.month(year, month))
