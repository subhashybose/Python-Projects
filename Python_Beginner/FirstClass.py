class FirstClass:
    num = 12
    name = "Subhash"
    town = 'Nalgonda'
    country = "India"
    salary = 1234.567

    def __init__(self):
        pass
        
    def __init__(self, num, name):
        self.num = num
        self.name = name

    def __str__(this):
        return f"{this.num} - {this.name}"

print(f"\nWelcome to My First Python Class \n")
"""
obj = FirstClass()
print(obj.num)
print(obj.name)
print(obj.town)
print(obj.country)
print(obj.salary)
"""
obj = FirstClass(9256, "Fairmont")

print(obj)
