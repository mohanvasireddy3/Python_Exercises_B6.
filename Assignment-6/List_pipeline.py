"""

# Task 1: String slicing and f-string formatting

# String reversal using slicing
text = "Python"
reversed_text = text[::-1]

print("Original:", text)
print("Reversed:", reversed_text)

# Required variables
msg = "hello"
model_name = "GPT"
version = 4

# Traditional concatenation
print(msg + " from " + model_name + "-version " + str(version) + "!")

# F-string formatting
print(f"{msg} from {model_name}-version {version}!")



# Task 2: Floating-point formatting

total_cost = 0.12345678

# Display 4 decimal places
print(f"Cost (4 decimal places): {total_cost:.4f}")

# Display 6 decimal places
print(f"Cost (6 decimal places): {total_cost:.6f}")



# Task 3: List initialization and utility inspection

# List containing different data types
sample_list = ["GPT4", True, 10, 10.20, "Gemini"]

# Empty lists
empty_list_1 = []
empty_list_2 = list()

# Display the lists
print("Sample list:", sample_list)
print("Empty list 1:", empty_list_1)
print("Empty list 2:", empty_list_2)

# Utility inspections
print("Type:", type(sample_list))
print("Length:", len(sample_list))
print("ID:", id(sample_list))

# Verify empty-list lengths
print("Length of empty_list_1:", len(empty_list_1))
print("Length of empty_list_2:", len(empty_list_2))



# Task 4: List indexing and IndexError handling

sample_list = ["GPT4", True, 10, 10.20, "Gemini"]

# Forward indexing
print("First element:", sample_list[0])
print("Second element:", sample_list[1])
print("Last element:", sample_list[4])

# Negative indexing
print("Last element:", sample_list[-1])
print("Second-to-last element:", sample_list[-2])
print("Third-to-last element:", sample_list[-3])

# Handling an out-of-bounds index
try:
    print(sample_list[5])
except IndexError:
    print("IndexError: list index out of range")




# Task 5: List mutability and ID tracking
sample_list = ["GPT4", True, 10, 10.20, "Gemini"]

# Record the initial ID
initial_id = id(sample_list)

print("Initial list:", sample_list)
print("Initial ID:", initial_id)

# Modify an existing element
sample_list[1] = False

# Display the modified list
print("Updated list:", sample_list)

# Record the ID after modification
updated_id = id(sample_list)

print("Updated ID:", updated_id)

# Compare the IDs
print("Same object:", initial_id == updated_id)



# Task 6: append(), extend(), and insert()

# 1. append() - add one element
sample_list = ["GPT4", True, 10]

sample_list.append("Gemini")

print("After append:", sample_list)
print("Length:", len(sample_list))

# 2. append() with a list
sample_list.append(["X", "Y", "Z"])

print("After appending a list:", sample_list)
print("Length:", len(sample_list))

# 3. extend() - add individual elements
sample_list = ["GPT4", True, 10]

sample_list.extend(["X", "Y", "Z"])

print("After extend:", sample_list)
print("Length:", len(sample_list))

# 4. insert() - add at a specific index
sample_list.insert(3, False)

print("After insert:", sample_list)
print("Length:", len(sample_list))



# Task 7: Nested lists and chained indexing

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, [9, 10]]
]

# Number of top-level elements
print("Length of matrix:", len(matrix))

# Retrieve 6 using two-level indexing
print("Value 6:", matrix[1][2])

# Retrieve 10 using three-level indexing
print("Value 10:", matrix[2][2][1])

"""

# Task 8: List deletion methods

# 1. pop() without an argument
sample_list = ["GPT4", True, 10, 20.5, "Gemini"]

removed = sample_list.pop()

print("After pop():")
print("Removed:", removed)
print("List:", sample_list)

# 2. pop(1)
sample_list = ["GPT4", True, 10, 20.5, "Gemini"]

removed = sample_list.pop(1)

print("\nAfter pop(1):")
print("Removed:", removed)
print("List:", sample_list)

# 3. pop(-2)
sample_list = ["GPT4", True, 10, 20.5, "Gemini"]

removed = sample_list.pop(-2)

print("\nAfter pop(-2):")
print("Removed:", removed)
print("List:", sample_list)

# 4. clear()
sample_list.clear()

print("\nAfter clear():")
print("List:", sample_list)
print("Length:", len(sample_list))
