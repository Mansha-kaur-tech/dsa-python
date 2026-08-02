# ----------------------------------------------
# Arrays - Basics
# ----------------------------------------------

# ----------------------------------------------
# 1. Creating an array
# ----------------------------------------------

# Note:
# Python doesn't have a built-in fixed-size array.
# In DSA, we'll use Python lists to represent arrays.
array = [1, 2, 3, 4, 5]

# ----------------------------------------------
# 2. Accessing elements in an array
# ----------------------------------------------

print(array[0])  # Access the first element
print(array[2])  # Access the third element
print(array[-1])  # Access the last element

# ----------------------------------------------
# 3. Modifying elements in an array
# -----------------------------------------------
array[1] = 10  # Modify the second element
print(array)  # Output: [1, 10, 3, 4, 5]    

array[-1] = 20  # Modify the last element
print(array)  # Output: [1, 10, 3, 4, 20]

# ----------------------------------------------
# 4. Adding elements to an array
# ----------------------------------------------    

array.append(6)  # Add an element at the end
print(array)  # Output: [1, 10, 3, 4, 20, 6]

array.insert(2, 15)  # Insert an element at index 2
print(array)  # Output: [1, 10, 15, 3, 4, 20, 6]

# ----------------------------------------------
# 5. Removing elements from an array
# ----------------------------------------------

array.remove(10)  # Remove the first occurrence of 10
print(array)  # Output: [1, 15, 3, 4, 20, 6]

array.pop()  # Remove the last element
print(array)  # Output: [1, 15, 3, 4, 20]

array.pop(1)  # Remove the element at index 1
print(array)  # Output: [1, 3, 4, 20]

# ----------------------------------------------
# 6. Iterating through an array
# ----------------------------------------------

for element in array:
    print(element)  # Output: 1, 3, 4, 20 (each on a new line)

# ----------------------------------------------
# 7. Finding the length of an array
# ----------------------------------------------

length = len(array)
print(length)  # Output: 4

# ----------------------------------------------
# 8. Checking if an element exists in an array
# ----------------------------------------------

if 3 in array:
    print("3 exists in the array")  # Output: 3 exists in the array
else:
    print("3 does not exist in the array")

print(5 in array)  # Output: False

# ----------------------------------------------
# 9. Copying an array
# ----------------------------------------------

array_copy = array.copy()  
print(array_copy)

# ----------------------------------------------
# 10. Clearing an array
# ----------------------------------------------

array.clear()  # Clear all the elements from the array
