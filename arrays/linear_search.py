# ------------------------------
# Linear Search
# ------------------------------

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1    # if the target isn't found in there then it prints -1


# ------------------------------
# Examples
# ------------------------------

print(linear_search([1, 2, 3, 4, 5], 3))  # returns 2)
print()
print(linear_search([1, 2, 3, 4, 5], 6))  # returns -1
print()
print(linear_search(['a', 'b', 'c', 'd'], 'd'))  # returns 2
print()