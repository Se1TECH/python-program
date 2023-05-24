# Calculate number of days between two dates
from datetime import date

firstDate = date(2023,2,2)
lastDate = date(2023,2,23)

diffe = lastDate - firstDate

print("Total days between this two dates are: " , diffe.days)
