'''
# Task 1: Set Comprehensions & PEP 8 String Normalization
# Uncleaned set of contributor names
names = {"alice", "BOB", "charlie", "DAVID"}

# Set comprehension to normalize names to title case
normalized_names = {name.capitalize() for name in names}

print("Original names:", names)
print("Normalized names:", normalized_names)

# Traditional multi-line for loop approach
normalized_names_loop = set()

for name in names:
    normalized_names_loop.add(name.capitalize())

print("Using for loop:", normalized_names_loop)

'''

'''
# Task 2: Dictionary Comprehensions — Transformation & Conditional Filtering
hyperparams = {
    "layers": 3,
    "units": 256,
    "dropout": 0.2
}

# 1. Value Scaling: Double all values
scaled_hyperparams = {
    k: v * 2
    for k, v in hyperparams.items()
}

print("Original hyperparameters:", hyperparams)
print("Scaled hyperparameters:", scaled_hyperparams)

# 2. Key Transformation & Conditional Filtering
filtered_hyperparams = {
    k.upper(): v
    for k, v in hyperparams.items()
    if v > 0.2
}
print("Filtered and uppercase keys:", filtered_hyperparams)

'''

'''

# Task 3: Combining Parallel Datasets using zip()

# Two parallel lists
years = [2020, 2021, 2022, 2023]
dataset_sizes = [100, 150, 200, 250]

# Combine the lists into a dictionary
yearly_dataset = dict(zip(years, dataset_sizes))

print("Years:", years)
print("Dataset sizes:", dataset_sizes)
print("Yearly dataset:", yearly_dataset)

'''
'''

# Task 4: Financial Metrics using Dictionary Comprehensions

sales = {
    2022: 50000,
    2023: 80000,
    2024: 120000
}

# Calculate 15% profit for each year
profits = {
    year: revenue * 0.15
    for year, revenue in sales.items()
}

print("Yearly sales:", sales)
print("Yearly profits:", profits)

'''

'''

# Task 5: Boolean Integer Representation & Arithmetic Operations

# Declare boolean variables
cardio_completed = True
strength_completed = False

# Add the boolean values
bonus_points = cardio_completed + strength_completed

print("Cardio completed:", cardio_completed)
print("Strength completed:", strength_completed)
print("Bonus points:", bonus_points)
print("Type of bonus_points:", type(bonus_points))

# Use the result in a conditional statement
if bonus_points > 0:
    print("Bonus points earned!")
else:
    print("No bonus points earned.")

'''

# Task 6: String Truthiness & Logical Operators

# 1. String Truthiness

empty_string = ""
non_empty_string = "Python"

if empty_string:
    print("Empty string is True")
else:
    print("Empty string is False")

if non_empty_string:
    print("Non-empty string is True")
else:
    print("Non-empty string is False")

# 2. AND Short-Circuiting

def second_condition():
    print("Second condition was evaluated.")
    return True

print("\nAND short-circuiting:")

if False and second_condition():
    print("AND condition is True")
else:
    print("AND condition is False")

# 3. OR Evaluation

print("\nOR evaluation:")

if False or second_condition():
    print("OR condition is True")
else:
    print("OR condition is False")


# 4. NOT with OR and Comparison

age = 16
has_consent = False

result = not (age >= 18 or has_consent)

print("\nNOT expression:")
print("Age:", age)
print("Has consent:", has_consent)
print("Result:", result)

if result:
    print("Access is denied.")
else:
    print("Access may be allowed.")