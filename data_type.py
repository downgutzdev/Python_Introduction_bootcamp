# data_type.py 

'''
Data types in Python
This file demonstrates the basic Python built-in data types  
- Strings are text surrounded by quotes.
- Integers are whole numbers, floats are decimals, and complex numbers have a real and imaginary part.
- Lists can be changed after creation, tuples cannot.
- A range generates numbers from start to stop (default starts at 0).
- Dictionaries store data in key-value pairs.
- Sets store unique items without order; frozensets cannot be modified.
- Booleans represent logical values True or False.
'''



# Text Type
text_example = "Hello, World!"          # str (string)
print(text_example)


# Numeric Types
integer_example = 42                    # int (integer number)
print(integer_example)

float_example = 3.14                     # float (decimal number)
print(float_example)

complex_example = 2 + 3j                  # complex (real + imaginary part)
print(complex_example)


# Sequence Types
list_example = [1, 2, 3, 4, 5]            # list (mutable sequence)
print(list_example)

tuple_example = (10, 20, 30)              # tuple (immutable sequence)
print(tuple_example)

range_example = range(5)                  # range (sequence of numbers)
print(list(range_example))


# Mapping Type
dict_example = {                          # dict (key-value mapping)
    "name": "Alice",
    "age": 25,
    "is_student": True
}
print(dict_example)


# Set Types
set_example = {1, 2, 3, 3, 2}             # set (unordered, unique elements)
print(set_example)

frozen_set_example = frozenset([4, 5, 6]) # frozenset (immutable set)
print(frozen_set_example)


# Boolean Type
bool_example_true = True                  # bool (true value)
print(bool_example_true)

bool_example_false = False                # bool (false value)
print(bool_example_false)
