# string_to_hex_utf8.py
from ast import literal_eval
str = "0xAAA"

# convert the string to the integer
convert_str = literal_eval(str)

# print the value and type of the convert_str
print(convert_str)
print("type", type(convert_str))

# pass the convert_str to the hex () method
hex_value = hex(convert_str)
print(hex_value)

# chcking the type of the value
print(type(hex_value))

