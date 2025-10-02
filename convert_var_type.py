# convert_var_type.py

'''
Variable Type Conversion in Python

- Convert int to float:
  Use float() around the integer value.

- Convert float to int:
  Use int() around the float value (it drops the decimal part).

- Convert by division:
  Using "/" between integers produces a float.
  Using "//" between numbers produces an integer (floor division).

- Convert numeric to string:
  Use str() around the numeric value.

- Convert string to number:
  Use int() or float() around the string value.
  The string must contain a valid numeric value to be converted.
'''



# Int to Float
int_price = 10
print(f"The value {int_price} is an int value")

price = float(int_price)
print(f"The value after converting to float is {price}")


# Float to Int
float_price = 10.30
print(f"The value {float_price} is a float value")

price = int(float_price)  # decimal part is discarded
print(f"The value after converting to int is {price}")


# Division Conversion
price = 10
print(f"The original value of price is {price}")

print(f"The result of price / 2 is {price / 2} (converted to float)")
print(f"The result of price // 2 is {price // 2} (converted to int)")


# Numeric to String
price = 10.50
age = 28

print(str(price))  # convert float to string
print(str(age))    # convert int to string
print(f"The age is {age} and the price is {price}")


# String to Number
price = "10.50"
age = "28"

print(float(price))  # convert string to float
print(int(age))      # convert string to int
