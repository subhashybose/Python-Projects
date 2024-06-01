from icecream import ic

print("Python Uncommon Features")

# Trick 1 - Slicing
'''
lst = list(range(1,11))
str = "Hello World"

ic(lst)
ic(str)
slc3 = slice(None, None, 3)
slcM3 = slice(None, None, -3)

ic(lst[:5])
lst1 = lst[::-1]
print(list(lst[::-1])[:5])
ic(lst[::3])

ic(str[:5])
ic(str[::3])

ic(lst[slc3])
ic(lst[slcM3])

ic(str[slc3])
ic(str[slcM3])
'''

# Trick 2 - Pipeline
'''
# To Combine/Merge Sets - use Pipe
# To Combine/Merge Lists - use Plus

lst1 = [1,2,3,4,5]
lst2 = [4,5,6,7,8,9,10]

ic(lst1 + lst2)
ic(set(lst1) & set(lst2))

set_a = {1,2,3,4,5}
set_b = {6,7,8,9,10}
ic(set_a | set_b)

set_c = {1,2,3,4,5}
set_d = {4,5,6,7,8}
ic(set_c | set_d)
ic(set_c - set_d)
ic(set_d - set_c)

set_e = {3,4,5}
ic(set_c & set_d & set_e) # Only common elements/intersection

ic(set_c ^ set_d ^ set_e) # Only Unique elements
'''

# Trick 3 - Walrus Operator :=
'''
dict_obj:dict = {1: 'One', 2: 'Two', 3: 'Three'}

#obj = dict_obj.get(4)
#print(obj)

if obj := dict_obj.get(1):
    print(obj)


def test_walrus(x) -> str:
    return (x := x.upper() + " " + str(len(x)))

print(test_walrus('Ranish'))
'''

# Trick 4 - Callable
from typing import Callable

def print_w_type(obj: object) -> Callable:
    def pwt() -> str:
        return (str(type(obj)) + ":" + str(obj))

    return pwt

pwt = print_w_type('Ranish')
print(pwt())