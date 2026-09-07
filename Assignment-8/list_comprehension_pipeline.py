"""
# Task 1: List Concatenation & Memory Address Analysis
# Standard concatenation (+)
list1 = [1, 2, 3]
print("Original list1:", list1)
print("Original id(list1):", id(list1))

list1 = list1 + [4, 5]
print("After +:", list1)
print("Updated id(list1):", id(list1))


# Augmented assignment (+=)
list2 = [1, 2, 3]
print("\nOriginal list2:", list2)
print("Original id(list2):", id(list2))

list2 += [4, 5]
print("After +=:", list2)
print("Updated id(list2):", id(list2))

"""

"""
# Task 2: Iteration, Indentation Rules, & Membership Search
# For Loop Iteration
ip_list = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]

print("IP addresses:")
for ip in ip_list:
    print(ip)

# Membership Checking
target_ips = ["10.0.0.2", "10.0.0.5"]

print("\nMembership search:")
for ip in target_ips:
    if ip in ip_list:
        print(ip, "is present in ip_list")
    else:
        print(ip, "is not present in ip_list")

"""
"""
# Task 3: Direct Assignment vs. Shallow Copying
# Direct Assignment
list_a = ["Alice", "Bob", "Charlie"]
list_b = list_a

print("Before modifying list_b:")
print("list_a:", list_a)
print("list_b:", list_b)
print("id(list_a):", id(list_a))
print("id(list_b):", id(list_b))

list_b.append("David")

print("\nAfter modifying list_b:")
print("list_a:", list_a)
print("list_b:", list_b)
print("id(list_a):", id(list_a))
print("id(list_b):", id(list_b))


# Shallow Copying
list_c = list_a.copy()

print("\nBefore modifying list_c:")
print("list_a:", list_a)
print("list_c:", list_c)
print("id(list_a):", id(list_a))
print("id(list_c):", id(list_c))

list_c.append("Eve")

print("\nAfter modifying list_c:")
print("list_a:", list_a)
print("list_c:", list_c)
print("id(list_a):", id(list_a))
print("id(list_c):", id(list_c))

"""

# Task 4: List Comprehensions

# Syntax Framework
# [expression for item in iterable if condition]

# Numerical Filtering
numbers = [2, 5, 7, 10, 14, 18, 21, 25]

greater_than_5 = [num for num in numbers if num > 5]
print("Numbers greater than 5:", greater_than_5)

divisible_by_7 = [num for num in numbers if num % 7 == 0]
print("Numbers divisible by 7:", divisible_by_7)


# String Normalization
contributors = ["alice", "BOB", "charlie", "dAVID"]

capitalized_names = [name.capitalize() for name in contributors]
print("Capitalized names:", capitalized_names)

lowercase_names = [name.lower() for name in contributors]
print("Lowercase names:", lowercase_names)


# Dataset Intersection
ai_team = ["Alice", "Bob", "Charlie", "David"]
data_team = ["Bob", "David", "Eve", "Frank"]

common_members = [name for name in ai_team if name in data_team]
print("Common team members:", common_members)


