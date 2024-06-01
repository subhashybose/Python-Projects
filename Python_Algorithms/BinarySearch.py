print("Python: Basic Search Program")


def performsort(lst):
    length = len(lst)
    for _ in range(length):
        for i in range(length):
            first = lst[i]
            if (i + 1) < length:
                nextval = lst[i + 1]
                if first > nextval:
                    lst[i] = nextval
                    lst[i + 1] = first


def recurloop():
    pass

lst = [90, 50, 20, 40, 100, 10, 70, 80, 60, 30]
print(f"Unsorted List: {lst}")

performsort(lst)

print(f"Sorted List: {lst}")

num = int(input("Enter a Number to Search"))
result = 'Not Found'

mid_lst_len = len(lst) // 2

if lst[mid_lst_len] == num:
    result = 'Found'
elif lst[mid_lst_len] > num:
    for i in range(mid_lst_len):
        if lst[i] == num:
            result = 'Found'
elif lst[mid_lst_len] < num:
    x = mid_lst_len
    for x in range(len(lst)):
        if lst[x] == num:
            result = 'Found'

print("Result => " + result)