# ---------------------------------------
# Tuples in Python
# ---------------------------------------

# ---------------------------------------
# 1. Creating a tuple
# ---------------------------------------

tuple1=(1, 3, 4, 6, 7, 8, 9, 10)
tuple2=("Alice", "Bob", "Charlie")
tuple3=(1, "Hello", 2.5, True)

tuple11=(1) 
print(type(tuple11))

# A single element tuple must have a trailing comma, otherwise it will be considered as an integer.

tuple12=(1,)
print(type(tuple12))

# ---------------------------------------
# 2. Accessing elements in a tuple
# ---------------------------------------

print(tuple1[0])
print(tuple2[2])
print(tuple3[-1])

# ---------------------------------------
# 3. Updating elements in a tuple
# ---------------------------------------


# tuple1[0] = 100

# TypeError:
# 'tuple' object does not support item assignment
# Tuples are immutable, so we cannot update elements in a tuple.

# ---------------------------------------
# 4. Concatenation of tuples
# ---------------------------------------

tuple4=tuple1+tuple2
print(tuple4)

# ---------------------------------------
# 5. Repetition of tuples
# ---------------------------------------

tuple5=tuple2*3
print(tuple5)

# ---------------------------------------
# 6. Slicing of tuples
# ---------------------------------------

tuple6=tuple1[2:5]
print(tuple6)

tuple7=tuple2[:2]
print(tuple7)

tuple8=tuple3[1:]
print(tuple8)

# ---------------------------------------
# 7. Length of a tuple
# ---------------------------------------

print(len(tuple1))
print(len(tuple2))
print(len(tuple3))

# ---------------------------------------
# 8. Membership testing in a tuple
# ---------------------------------------

print(3 in tuple1)
print("Alice" in tuple2)
print("Hello" in tuple3)    

# ---------------------------------------
# 9. Iterating through a tuple
# ---------------------------------------

for item in tuple1:
    print(item)

for item in tuple2:
    print(item)

for item in tuple3:
    print(item)

# ---------------------------------------
# 10. count() and index() methods in a tuple
# ---------------------------------------

print(tuple1.count(3))
print(tuple2.index("Bob"))

# ---------------------------------------
# 11. Deleting a tuple
# ---------------------------------------

del tuple1
# print(tuple1)

# NameError:
# name 'tuple1' is not defined