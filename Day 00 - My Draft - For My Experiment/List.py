# Due to reference assignment properties if print out List2 and List1 get same result.
# some people said if data type is not primitive data type (int, float,string and bool) then we should get reference assignment properties effect.

List1 = [1,2,3]
List2 = List1
List1.append(4)

print(List2)
print(List1)

# In Python, when you assign one list to another (e.g., List2 = List1), both variables point to the same list object in memory. As a result, modifying one (e.g., appending an element) affects the other. This is due to Python's reference assignment behavior for mutable objects like lists.

# To prevent this and create an independent copy of the list, you can use one of the following methods:
# 1. Use Slicing

List1 = [1, 2, 3]
List2 = List1[:]
List1.append(4)

print(List1)  # Output: [1, 2, 3, 4]
print(List2)  # Output: [1, 2, 3]

# 2. Use the copy() Method

List1 = [1, 2, 3]
List2 = List1.copy()
List1.append(4)

print(List1)  # Output: [1, 2, 3, 4]
print(List2)  # Output: [1, 2, 3]

# 3. Use the list() Constructor

List1 = [1, 2, 3]
List2 = list(List1)
List1.append(4)

print(List1)  # Output: [1, 2, 3, 4]
print(List2)  # Output: [1, 2, 3]

# 4. Use deepcopy() for Nested Lists

# If the list contains nested lists (or other mutable objects), a shallow copy (methods above) will not suffice. Use the copy.deepcopy() method for a complete independent copy.

import copy

List1 = [[1, 2], [3, 4]]
List2 = copy.deepcopy(List1)
List1[0].append(5)

print(List1)  # Output: [[1, 2, 5], [3, 4]]
print(List2)  # Output: [[1, 2], [3, 4]]

# Explanation of Methods

#     Slicing ([:]): Creates a shallow copy by slicing the entire list.
#     copy() Method: Also creates a shallow copy, making it equivalent to slicing.
#     list() Constructor: Converts the original list into a new list object, providing a shallow copy.
#     copy.deepcopy(): Ensures a complete deep copy, useful for complex, nested data structures.