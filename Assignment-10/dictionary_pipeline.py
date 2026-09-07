'''
# Task 1: Frozen Set vs. Standard Set Recap

# 1. Standard mutable set
set_x = {1, 2, 3}

print("Standard set:", set_x)

# Sets allow adding and removing elements
set_x.add(4)
print("After add(4):", set_x)

set_x.remove(2)
print("After remove(2):", set_x)

# Sets do not support index-based access
try:
    print(set_x[0])
except TypeError as e:
    print("Index access error:", e)


# 2. Create a frozenset from a list containing duplicates
data = [1, 2, 2, 3, 3, 4, 4]

frozen_x = frozenset(data)

print("Original list:", data)
print("Frozen set:", frozen_x)


# 3. Verify that frozenset cannot be modified
try:
    frozen_x.add(5)
except AttributeError as e:
    print("frozenset add() error:", e)

try:
    frozen_x.remove(1)
except AttributeError as e:
    print("frozenset remove() error:", e)
'''

'''
# Task 2: Dictionary Declaration, Key Rules, & Unhashable Type Errors

# 1. Dictionary with different immutable key types
model_config = {
    "model_name": "GPT4",
    1: "version_1",
    True: "active",
    (1, 2): "coordinates"
}

print("Model configuration:")
print(model_config)


# 2. Access values using their keys
print("Model name:", model_config["model_name"])
print("Version:", model_config[1])
print("Status:", model_config[True])
print("Coordinates:", model_config[(1, 2)])


# 3. Attempt to use a list as a dictionary key
try:
    invalid_config = {
        [1, 2, 3]: "invalid"
    }
except TypeError as e:
    print("Exception:", e)


# 4. Dictionary syntax reminder
print("\nDictionary syntax:")
print("Colon (:) separates a key from its value.")
print("Comma (,) separates individual key-value pairs.")
print("Comma is the king!")

'''

'''
# Task 3: Accessing Values, Safe Fetching (.get()), & Duplicate Key Overwriting
# 1. Declare hyperparameters dictionary
hyperparameters = {
    "learning_rate": 0.01,
    "dropout_rate": 0.23,
    "optimizer": "adam"
}

# Access an existing key
print("Optimizer:", hyperparameters["optimizer"])


# Attempt to access a missing key safely using try-except
try:
    print("Dropout:", hyperparameters["dropout"])
except KeyError as e:
    print("KeyError:", e)


# 2. Safe fetching using .get()
dropout = hyperparameters.get("dropout", "Key not found")
print("Safe dropout lookup:", dropout)

# Existing key with .get()
dropout_rate = hyperparameters.get("dropout_rate", "Key not found")
print("Existing dropout_rate:", dropout_rate)


# 3. Duplicate key assignment / overwriting
hyperparameters["dropout_rate"] = 0.3
print("After first assignment:", hyperparameters["dropout_rate"])

hyperparameters["dropout_rate"] = 0.6
print("After second assignment:", hyperparameters["dropout_rate"])

print("Final hyperparameters:", hyperparameters)

'''

'''
# Task 4: Nested Dictionaries & Chained Key Lookups
# 1. Create a nested dictionary for multiple models
pipeline_config = {
    "GPT4": {
        "layers": 48,
        "parameters": "1.76T",
        "attention_heads": 96
    },
    "BERT": {
        "layers": 24,
        "parameters": "340M",
        "attention_heads": 16
    },
    "Opus4": {
        "layers": 80,
        "parameters": "500B",
        "attention_heads": 128
    }
}

print("Pipeline Configuration:")
print(pipeline_config)


# 2. Extract parameters for BERT
bert_parameters = pipeline_config["BERT"]["parameters"]
print("BERT parameters:", bert_parameters)


# 3. Extract layers for GPT4
gpt4_layers = pipeline_config["GPT4"]["layers"]
print("GPT4 layers:", gpt4_layers)

'''

'''
# Task 5: Dictionary Copying (Assignment vs. .copy()), .clear(), & Merging
# 1. Direct Assignment - Both variables refer to the same dictionary
model_params = {
    "learning_rate": 0.01,
    "batch_size": 32,
    "epochs": 10
}
shared_params = model_params
print("Original model_params:", model_params)

# Modify shared_params
shared_params["learning_rate"] = 0.001
print("After modifying shared_params:")
print("shared_params:", shared_params)
print("model_params:", model_params)

# 2. Shallow Copy using .copy()
safe_params = model_params.copy()

# Clear the original dictionary
model_params.clear()
print("\nAfter clearing model_params:")
print("model_params:", model_params)
print("safe_params:", safe_params)

# 3. Merge dictionaries using .update()
base_config = {
    "learning_rate": 0.01,
    "batch_size": 32,
    "epochs": 10
}
version_config = {
    "epochs": 20,
    "optimizer": "adam",
    "dropout": 0.2
}
print("\nBefore update:")
print("base_config:", base_config)
print("version_config:", version_config)

# Merge version_config into base_config
base_config.update(version_config)
print("\nAfter update:")
print("base_config:", base_config)

'''


'''
# Task 6: Inspection Methods, Tuple Unpacking, & Bitwise Set Operators
# Dictionary for inspection
config = {
    "model": "GPT4",
    "batch_size": 32,
    "epochs": 20,
    "optimizer": "adam"
}

# 1. Keys, Values, and Items
print("Keys:", config.keys())
print("Values:", config.values())
print("Items:", config.items())


# 2. Loop through items using tuple unpacking
print("\nKey-Value pairs:")
for key, value in config.items():
    print(f"{key} -> {value}")


# 3. Membership search
if "batch_size" in config.keys():
    print("\n'batch_size' key exists in config.")

if 32 in config.values():
    print("Value 32 exists in config.")


# 4. Dictionary key operations
config_a = {
    "model": "GPT4",
    "batch_size": 32,
    "epochs": 10
}
config_b = {
    "model": "BERT",
    "batch_size": 64,
    "optimizer": "adam"
}

# Intersection - common keys
common_keys = config_a.keys() & config_b.keys()
print("\nCommon keys:", common_keys)

# Union - all unique keys
all_keys = config_a.keys() | config_b.keys()
print("All unique keys:", all_keys)

'''


# Task 7: Item Deletion Methods — .pop(), .popitem(), and .clear()
# Create a sample dictionary
data = {
    "name": "Mohan",
    "age": 22,
    "city": "Hyderabad",
    "role": "Developer"
}
print("Original dictionary:", data)

# 1. Targeted Removal using .pop(key)
removed_age = data.pop("age")
print("\nRemoved age:", removed_age)
print("After pop('age'):", data)

# Calling .pop() without an argument raises an error
try:
    data.pop()
except TypeError as e:
    print("Error when calling pop() without arguments:", e)

# 2. Last-Item Removal using .popitem()
last_item = data.popitem()
print("\nRemoved last item:", last_item)
print("After popitem():", data)

# 3. Full Wipe using .clear()
data.clear()
print("\nAfter clear():", data)

