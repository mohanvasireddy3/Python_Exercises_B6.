"""
name="Mohan"
age=24
print("before concatenation" +name)
name="Vasireddy"
print(age)

print("after concatenation" +name)

temperature, user_age, a=30, 24, 'a value'
print(temperature, user_age, a)

"""
# Case sensitivity in python
"""
name="Mohan"
Name, age= "vasireddy", 24
print(Name, age)
print(name)

name="Mohan"
Name, age= "vasireddy", 24
print(name, age)
print(Name)
"""

#this script contains PEP 8 commenting standards.

counter = 0

user_age = 24

discount = 0.15 if user_age < 25 else 0.05

counter += 1

is_verified = True
is_active =False

if is_verified:

    is_active =True

print("counter:", counter)
print("Discount:", discount)
print("Account Active:", is_active)
