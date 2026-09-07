"""
# Task 1: Tuple Definition, Immutability, and Single-Element Syntax
# Tuple initialization
location = (37.7749, -122.4194)
print("Location:", location)
print("Location type:", type(location))
# Immutability test
try:
    location[1] = -122.5000
except TypeError as e:
    print("Immutability error:", e)

# Single value without a comma -> int
single_val1 = (10)
print("single_val1:", single_val1)
print("single_val1 type:", type(single_val1))

# Single value with a trailing comma -> tuple
single_val2 = (10,)
print("single_val2:", single_val2)
print("single_val2 type:", type(single_val2))

"""

"""
# Task 2: Explicit Type Casting (list <-> tuple) and Data Freezing

# Mutable list of scores
score_list = [85, 90, 78, 92, 88]
print("Original score list:", score_list)
print("score_list type:", type(score_list))

# Convert list to immutable tuple
immutable_scores = tuple(score_list)
print("Immutable scores:", immutable_scores)
print("immutable_scores type:", type(immutable_scores))

# Verify tuple immutability
try:
    immutable_scores[0] = 100
except TypeError as e:
    print("Modification error:", e)

# Attempt to add an element
try:
    immutable_scores.append(95)
except AttributeError as e:
    print("Addition error:", e)

# Convert tuple back to a list
mutable_scores = list(immutable_scores)
print("Converted back to list:", mutable_scores)
print("mutable_scores type:", type(mutable_scores))

"""

"""
# Task 3: Tuple Unpacking and Multi-Dimensional Nested Tuple Access

# Tuple unpacking
location = (37.7749, -122.4194)
latitude, longitude = location

print("Latitude:", latitude)
print("Longitude:", longitude)

# Define a 2D nested tuple matrix
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Extract target values using chained indexing
value_5 = matrix[1][1]
value_8 = matrix[2][1]

print("Value 5:", value_5)
print("Value 8:", value_8)

"""

"""

# Task 4: Set Fundamentals, Uniqueness, and Empty Set Declaration

# Set with duplicate values
unique_ids = {1, 2, 3, 3, "A", "B", 4}

print("Unique IDs:", unique_ids)
print("Number of unique IDs:", len(unique_ids))

# Empty curly braces create a dictionary
empty_1 = {}
print("empty_1:", empty_1)
print("empty_1 type:", type(empty_1))

# set() creates an empty set
empty_2 = set()
print("empty_2:", empty_2)
print("empty_2 type:", type(empty_2))

"""

"""
# Task 5: List Deduplication and Set Modification Methods

# One-line list deduplication
duplicate_log = ["hello", "world", "hello", "python", "world"]
clean_log = list(set(duplicate_log))

print("Original log:", duplicate_log)
print("Clean log:", clean_log)

# Set for modification demonstrations
unique_ids = {1, 2, 3, 4}

# .add() - add a single element
unique_ids.add(5)
print("After add(5):", unique_ids)

# .remove() - remove an element
unique_ids.remove(3)
print("After remove(3):", unique_ids)

# .update() - add multiple elements
unique_ids.update([6, 7, 8])
print("After update([6, 7, 8]):", unique_ids)

# Item assignment rejection
try:
    unique_ids[0] = 99
except TypeError as e:
    print("Assignment error:", e)

"""

"""
# Task 6: Immutable Set Management using frozenset()

# Create an immutable set
static_set = frozenset([1, 2, 3, 3, 4])

# Print the frozenset
print("Static set:", static_set)
print("Static set type:", type(static_set))

# Attempt to modify the frozenset
try:
    static_set.add(5)
except AttributeError as e:
    print("Modification error:", e)

"""

# Task 7: Tuple Slicing, Sequence Reversal, and Tuple Comprehension

# Define a tuple
data_tuple = (1, 2, 3, 4, 5)

# Extract elements 2, 3, and 4
middle_values = data_tuple[1:4]
print("Sliced tuple:", middle_values)

# Reverse the tuple
reversed_tuple = data_tuple[::-1]
print("Reversed tuple:", reversed_tuple)

# Filter even numbers and explicitly cast the result to a tuple
even_tuple = tuple(num for num in data_tuple if num % 2 == 0)
print("Even tuple:", even_tuple)



