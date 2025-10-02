# input_output_functions.py

'''
Input and Output in Python

- input(prompt) shows an optional prompt (a string) and returns what the user types as a string.
- To use numbers from input, convert the string with int() or float().
- print(...) writes text to the screen (standard output). All given objects are converted to strings.
  Useful parameters:
  - sep: text placed between multiple items (default: " ")
  - end: text appended at the end (default: "\n")
  - flush: if True, forces immediate display (default: False)
'''

# Basic input (string)
name = input("Type your name: ")
print(f"Your name is {name}, correct?")

# Input converted to number
age_str = input("Type your age (number): ")
age = int(age_str)           # convert input string to int
print(f"In 5 years, you will be {age + 5}.")

# print with sep and end
first_name = "Guilherme"
last_name = "Carvalho"

print(first_name, last_name)                 # default: sep=" ", end="\n"
print(first_name, last_name, sep="#")        # custom separator
print("Loading", end="...")                  # custom end (no newline yet)
print(" done!")                              # next print completes the line
