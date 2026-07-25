# ---------------------------------------
# Sets in Python
# ---------------------------------------

# ---------------------------------------
# 1. Creating a set
# ---------------------------------------

set1 = {1, 3, 4, 6, 7, 8, 9, 10, 3, 4, 5}
set2 = {"Hello", "World", "Python"}
set3 = set()  # Empty set

print(set1)
print(set2)
print(set3)

# ---------------------------------------
# 2. Adding elements to a set
# ---------------------------------------

set1.add(11)
set2.add("Programming")
set1.add(1)

print(set1)
print(set2)

# ---------------------------------------
# 3. Removing elements from a set
# ---------------------------------------

set1.remove(6)
set2.discard("World")

print(set1)
print(set2)

# ---------------------------------------
# 4. Membership testing in a set
# ---------------------------------------

print(3 in set1)
print("Python" in set2)

# ---------------------------------------
# 5. Length of a set
# ---------------------------------------

print(len(set1))
print(len(set2))
print(len(set3))

# ---------------------------------------
# 6. Iterating through a set
# ---------------------------------------

for element in set1:
    print(element)

for element in set2:
    print(element)

# ---------------------------------------
# 7. Duplicate removal in a set
# ---------------------------------------

# Sets automatically remove duplicates

# ---------------------------------------
# 8. Intersection of sets
# ---------------------------------------

set4 = {1, 2, 3, 4, 5}
set5 = {4, 5, 6, 7, 8}

intersection = set4 & set5
print(intersection)

# ---------------------------------------
# 9. Union of sets
# ---------------------------------------

union = set4 | set5
print(union)

# ---------------------------------------
# 10. Difference of sets
# ---------------------------------------

difference = set4 - set5
print(difference)   

# ---------------------------------------
# 11. Symmetric difference of sets
# ---------------------------------------

symmetric_difference = set4 ^ set5
print(symmetric_difference)

# ---------------------------------------
# 12. Clearing a set
# ---------------------------------------

set1.clear()
print(set1)

# ---------------------------------------
# 13. Frozen sets
# ---------------------------------------

frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set)