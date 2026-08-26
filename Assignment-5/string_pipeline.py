# Task 1: Case Conversions & Text Normalization
"""

model_output = "aI is the Future of Everything"

uppercase_output = model_output.upper()
lowercase_output = model_output.lower()
capitalize_output = model_output.capitalize()
title_output = model_output.title()

print("Original     :", model_output)
print("Uppercase    :", uppercase_output)
print("Lowercase    :", lowercase_output)
print("Capitalize   :", capitalize_output)
print("Title        :", title_output)
"""
"""
# Task 2: Whitespace & Character Stripping

response = "   ???Hello Human???   "

# Remove leading and trailing whitespace
strip_default = response.strip()

# Remove leading/trailing spaces and question marks
strip_custom = response.strip(" ?")

print("Original response :", repr(response))
print("strip()           :", repr(strip_default))
print('strip(" ?")       :', repr(strip_custom))

"""
"""
# Task 3: Substring Replacement & Case-Insensitive Counting

text = "ML is a critical component of the modern AI. ML techniques are advancing rapidly."

# Replace every occurrence of "ML" with "Machine Learning"
replaced_text = text.replace("ML", "Machine Learning")

print("Original text :", text)
print("Replaced text :", replaced_text)

count_text = "AI is the Future. Embrace the future of AI."

# Case-sensitive count
case_sensitive_count = count_text.count("future")

# Case-insensitive count
case_insensitive_count = count_text.lower().count("future")

print("Case-sensitive count of 'future' :", case_sensitive_count)
print("Case-insensitive count of 'future':", case_insensitive_count)

"""
"""
# Task 4: String Splitting, Joining, Prefix/Suffix Removal, & Immutability

# 1. Splitting
sentence = "a breakthrough at every step"
words = sentence.split()

print("Split result :", words)
print("Object type  :", type(words))

# 2. Joining
terms = ['AI', 'ML', 'genai', 'LLM', 'NLP']
joined_terms = ", ".join(terms)

print("Joined result:", joined_terms)

# 3. Prefix removal
url = "https://example.com"
clean_url = url.removeprefix("https://")

print("Original URL :", url)
print("Clean URL    :", clean_url)

# Suffix removal
file_name = "state_of_AI_2025.pdf"
clean_file = file_name.removesuffix(".pdf")

print("Original file:", file_name)
print("Clean file   :", clean_file)

# 4. Proving string immutability
# Calling removesuffix() without assigning the result
# does NOT change the original string.
file_name.removesuffix(".pdf")

print("After direct removesuffix():", file_name)

# The returned value must be assigned to retain the change.
clean_file = file_name.removesuffix(".pdf")

print("Assigned clean file         :", clean_file)

# Direct item assignment is not allowed for strings.
message = "Hello"

try:
    message[0] = "X"
except TypeError as error:
    print("Item assignment error:", error)

"""

# Task 5: Indexing, Concatenation, Repetition, & Slicing

# 1. Indexing
message = "GenAI is amazing"

print("Message:", message)

# Forward indexing (0-based)
print("Character at index 0 :", message[0])
print("Character at index 1 :", message[1])
print("Character at index 5 :", message[5])

# Negative/reverse indexing
print("Last character (-1)  :", message[-1])
print("Character at (-8)    :", message[-8])

# 2. Concatenation
greeting = "Hello"
name = "AI"
version = 5

combined = greeting + " " + name + " " + str(version)

print("Concatenated string:", combined)

# 3. Repetition
separator = "=" * 30

print(separator)

# 4. Multi-parameter slicing
text = "machine learning"

# Extract "machine"
machine = text[0:7]
machine_short = text[:7]

# Extract characters from index 13 to the end
from_index_13 = text[13:]

# Extract alternative characters
every_second = text[::2]

# Reverse the entire string
reversed_text = text[::-1]

print("Original text       :", text)
print("text[0:7]           :", machine)
print("text[:7]            :", machine_short)
print("text[13:]           :", from_index_13)
print("text[::2]            :", every_second)
print("text[::-1]          :", reversed_text)