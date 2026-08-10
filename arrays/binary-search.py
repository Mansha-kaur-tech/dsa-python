# ---------------------------------
# Binary Search
# ---------------------------------

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# ---------------------------------
# Examples
# ---------------------------------

print(binary_search([1, 2, 3, 4, 5], 3))  # returns 2
print()
print(binary_search([1, 2, 3, 4, 5], 6))  # returns -1
print()
print(binary_search(['a', 'b', 'c', 'd'], 'd'))  # returns 3
print()
print(binary_search(['a', 'b', 'c', 'd'], 'a'))  # returns 0
print()
arr = [7, 1, 3, 9, 5]
print(binary_search(arr, 7))  # returns 2