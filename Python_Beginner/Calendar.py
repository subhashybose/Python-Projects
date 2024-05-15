import calendar

print ("Print Calendar Month")

year = int(input("Enter Year: "))
month = int(input("Enter Month: "))
print("\n")
cal = calendar.month(year, month)

print(cal)
