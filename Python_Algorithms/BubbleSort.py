print ("Python: Basic Sort Program")

#lst_nums = ['30', '20', '50', '10', '40']
lst_nums = []

class TestSort:
    def sort(self, lst_nums):
        length = len(lst_nums)
        for _ in range(length):
            for i in range(length):
                first = lst_nums[i]
                if (i+1) < length:
                    next = lst_nums[i+1]
                    if first > next:
                        lst_nums[i] = next
                        lst_nums[i+1] = first

    def add(self, lst_nums, num):
        lst_nums.append(num)


obj = TestSort()
tot_num = int(input("Total Numbers to be Sorted: "))
for _ in range(tot_num):
    obj.add(lst_nums, int(input()))


print (f"Before Sort: {lst_nums}")
obj.sort(lst_nums)
print (f"After Sort: {lst_nums}")
