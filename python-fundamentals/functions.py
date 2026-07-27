# ----------------------------------------------
# Functions in Python
# ----------------------------------------------

# ----------------------------------------------
# 1. Creating a Function
# ----------------------------------------------

def hello():
    print("Hello, World!")
    return "Function executed"

result = hello()  # Calling the function and storing the return value
print(result)

# ----------------------------------------------
# 2. Calling a Function
# ----------------------------------------------

result = hello()
hello()  # Calling the function again

# ----------------------------------------------
# 3. Function with Parameters
# ----------------------------------------------

def student_info(name, age):
    print(f"Name: {name}, Age: {age}")

student_info("Mansha", 18)

def add_numbers(a, b):
    return a + b

add_numbers(5, 10)
print(add_numbers(5, 10))  # Output: 15

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()  # Uses default parameter
greet("Alice")  # Overrides default parameter

# ----------------------------------------------
# 4. Arguments and Keyword Arguments
# ----------------------------------------------

def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info("Mansha", 18)  # Positional arguments
display_info(age=18, name="Mansha")  # Keyword arguments

# ----------------------------------------------
# 5. Return statements
# ----------------------------------------------

def multiply(a, b):
    return a * b

result = multiply(5, 10)
print(result)

# ----------------------------------------------
# 6. Variable Scope
# ----------------------------------------------

x = 10  # Global variable
def my_function():
    x = 5  # Local variable
    print("Local x:", x)
    
my_function()
print("Global x:", x)

# ----------------------------------------------
# 7. Lambda Functions
# ----------------------------------------------

square = lambda x: x ** 2
print(square(5))  # Output: 25

# ----------------------------------------------
# 8. Recursion
# ----------------------------------------------

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120