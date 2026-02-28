# dry.py - Built-in Functions Demo

# 1. print() - Displays output to the console
print("Hello, World!")

# 2. len() - Returns the number of items in an object
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # 3

# 3. range() - Generates a sequence of numbers
for i in range(5):
    print(i)

# 4. type() - Returns the data type of an object
print(type(42))       # <class 'int'>
print(type("hello"))  # <class 'str'>

# 5. sorted() - Returns a new sorted list from an iterable (NEW!)
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]
