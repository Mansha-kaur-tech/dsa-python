# --------------------------------
# Dictionary in Python
# --------------------------------  

# ---------------------------------------
# 1. Creating a dictionary
# ---------------------------------------

dict1 = {"name": "Alice", "age": 25, "city": "New York"}
dict2 = {1: "one", 2: "two", 3: "three"}

# ----------------------------------------
# 2. Accessing values in a dictionary
# ----------------------------------------

print(dict1["name"])
print(dict1[2])
print(dict2.get("age"))  # Produce none as outputdue to inavailability of that key 

# ---------------------------------------
# 3. Updating values in a dictionary
# ---------------------------------------

dict1["age"] = 26
dict2[3] = "three updated"
print(dict1)
print(dict2)

# ---------------------------------------
# 4. Adding new key-value pairs to a dictionary
# ---------------------------------------

dict1["occupation"] = "Engineer"
dict2[4] = "four"
print(dict1)
print(dict2)

# ---------------------------------------
# 5. Removing key-value pairs from a dictionary
# ---------------------------------------

del dict1["city"]
dict2.pop(2)
print(dict1)
print(dict2)

# ---------------------------------------
# 6. Iterating through a dictionary
# ---------------------------------------

for key in dict1:
    print(key, dict1[key])

for key, value in dict2.items():
    print(key, value)

# ---------------------------------------
# 7. Length of a dictionary
# ---------------------------------------

print(len(dict1))
print(len(dict2))

# ---------------------------------------
# 8. Membership testing in a dictionary
# ---------------------------------------

print("name" in dict1)
print(2 in dict2)

# ---------------------------------------
# 9. Dictionary methods
# ---------------------------------------

print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(dict2.keys())
print(dict2.values())
print(dict2.items())

# ---------------------------------------
# 10. Clearing a dictionary
# ---------------------------------------

#dict1.clear()    # This will remove all items from dict1 
#dict2.clear()    

# ---------------------------------------
# 11. Deleting a dictionary
# ---------------------------------------

#del dict1    # This will delete the dictionary dict1

# ---------------------------------------
# 12. Nested dictionaries
# ---------------------------------------

nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

print(nested_dict["person1"]["name"])
for person, details in nested_dict.items():
    print(person, details)