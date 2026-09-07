"""

numbers = [10, 20, 30, 40, 50, 60]

print("numbers[1:4]:", numbers[1:4])
print("numbers[:3]:", numbers[:3])
print("numbers[2:]:", numbers[2:])
print("numbers[::2]:", numbers[::2])
print("numbers[::-1]:", numbers[::-1])

"""
"""
sequence = [10, 20, 30, 40, 50]

sequence.reverse()
print("Reversed:", sequence)

unordered_list = [50, 20, 40, 10, 30]

unordered_list.sort()
print("Ascending:", unordered_list)

unordered_list.sort(reverse=True)
print("Descending:", unordered_list)

numbers = [30, 10, 20]
print("Return value of sort():", numbers.sort())
print("Sorted list:", numbers)

"""
"""
# Task 1: F-String & List Basics Recap

model = "GPT-4"
accuracy = 0.954321

print(f"Model: {model} | Accuracy: {accuracy:.2f}")

"""

"""

# Task 5: Advanced List Slicing [start:stop:step]

numbers = [3, 18, 21, 25, 30]

print("Original List:", numbers)
print("Extracted [19-21] (index 1 to pos 4):", numbers[1:4])
print("First 3 items [:3]:", numbers[:3])
print("Items from index 2 to end [2:]:", numbers[2:])
print("Every 2nd item [::2]:", numbers[::2])
print("Reversed List via Slicing [::-1]:", numbers[::-1])

"""
# Task 6: List Methods (.reverse() and .sort())

demo_list = [28, 29, 30, 31]

demo_list.reverse()
print("After .reverse():", demo_list)

unordered = [3, 25, 32]

unordered.sort()
print("Ascending .sort():", unordered)

unordered.sort(reverse=True)
print("Descending .sort(reverse=True):", unordered)


