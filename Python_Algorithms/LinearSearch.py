print ("Python: Basic Search Program")

lst = [10,20,30,40,50,60,70,80,90,100]
num = int(input("Enter a Number to Search"))
result = 'Not Found'
for i in range(len(lst)):
    if lst[i] == num:
        result = 'Found'

print ("Result => " + result)