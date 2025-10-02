# variables.py

'''
Variables and Constants in Python
This file demonstrates how to create and use variables in Python.

- Variables store data that can change during the program.
- Python does NOT have true constants. 
  By convention, we use UPPERCASE names to indicate a value that should not change.
- Assigning new values to a variable overwrites the old one.
- We can assign one or multiple variables at once.
- f-strings make it easy to include variables in text.
'''



# Variables
age = 23
name = "Guilherme"
print(f"My name is {name} and I am {age} years old.")

# Reassigning variables
age = 24  # age changed
print(f"Now I am {age} years old.")

# Multiple assignment
age, name = (25, "Alice")
print(f"My name is {name} and I am {age} years old.")


# Constant-like values (by convention)
PI = 3.14159          # treated as a constant by naming convention
APP_NAME = "My First Python App"
print(f"The constant-like PI is {PI}")
print(f"The application name is {APP_NAME}")

# Using these values in calculations
radius = 5
circle_area = PI * (radius ** 2)
print(f"The area of a circle with radius {radius} is {circle_area}")
