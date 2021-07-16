# string_to_hex.py

str = "245FC"

# pass the str to the int () to convert it into base16 int
base16INT = int(str, 16)

# print the converted string to base16 hexadecimal int value
print("value",base16INT)
print("value",type(base16INT))

hex_value = hex(base16INT)
print(hex_value)

# chcking the type of the value
print(type(hex_value))

