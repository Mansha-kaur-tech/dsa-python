# ---------------------------------------------
# Lists in Python
# ----------------------------------------------

# ---------------------------------------
# 1. Creating a list
# ---------------------------------------

list1=[1,3,4,6,7,8,9,10]
names=['John','Jane','Doe','Smith']
mix=["Hello",1,2.5,True]

# ---------------------------------------
# 2. Accessing elements in a list
# ---------------------------------------

print(list1[0]) 
print(names[3])
print(mix[-1])
print(list1[-3])

# ---------------------------------------
# 3. Updating elements in a list
# ---------------------------------------

mix[0]=100
list1[5]=200
names[2]="Alice"
print(list1)
print(names)
print(mix)

# ---------------------------------------
# 4. append()
# ---------------------------------------

list1.append(11)
names.append("Bob")
mix.append("World")
print(list1)
print(names)
print(mix)

# ---------------------------------------
# 5. insert()
# ---------------------------------------

list1.insert(2, 99)
names.insert(1, "Charlie")
mix.insert(3, False)
print(list1)
print(names)
print(mix)

# ---------------------------------------
# 6. remove()
# ---------------------------------------

list1.remove(6)
names.remove("Alice")
mix.remove(2.5)
print(list1)
print(names)
print(mix)

# ---------------------------------------
# 7. pop()
# ---------------------------------------

list1.pop()
names.pop()
mix.pop(1)
print(list1)
print(names)
print(mix)

# ---------------------------------------
# 8. len()
# ---------------------------------------

print(len(list1))
print(len(names))
print(len(mix))

# ---------------------------------------
# 9. sort()
# ---------------------------------------

list1.sort()
names.sort()    
print(list1)
print(names)

# ---------------------------------------
# 10. reverse()
# ---------------------------------------

list1.reverse()
names.reverse()
print(list1)
print(names)


