import calendar
"""
print ("Print Calendar Month")

year = int(input("Enter Year: "))
month = int(input("Enter Month: "))
print("\n")
cal = calendar.month(year, month)

print(cal)

"""

print ("Loop Calendar Days")
#itr = calendar.iterweekdays()
#print (next(itr))

list = ("A", "B", "C", "D")
itr = iter(list)

print (next(itr))

for i in list:
    print(i)
