# str_to_hexa_using_ast_literal_eval.py

from ast import literal_eval
# convert the string to the bytes
str= 'linuxhint'.encode('utf-8')

# print the converted string to bytes
print(str)

# convert the string bytes to the hexadecimal string
hex_str = str.hex()

# print the converted hexadecimal value type
print(type(hex_str))
