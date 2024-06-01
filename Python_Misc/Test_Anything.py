print ("Welcome to Python again...")
# loop a list
strArr = ['a', 'b', 'c', 'd', 'e']
for s in strArr:
    print (s)

# division for reminder
print(11 // 2)

# list concatenation
lst1 = [1,2,3,4,5]
lst2 = [4,5,6,7,8,9,10]

print( lst1 + lst2 )

# lambda expressions
dict_obj = {1: 'One', 2: 'Two'}

dict_get = lambda d, i : d.get(i)
print(dict_get(dict_obj, 1))
