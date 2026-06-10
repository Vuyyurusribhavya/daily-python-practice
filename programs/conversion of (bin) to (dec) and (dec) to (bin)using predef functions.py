# | Conversion       | Function used    |
# | ---------------- | ---------------- |
# | Decimal → Binary | `bin()`          |
# | Binary → Decimal | `int(binary, 2)` |







# # Write a Python program to convert a decimal number into binary using a predefined function.
# num = int(input("Enter a decimal number: "))

# binary = bin(num)

# print("Binary:", binary)

# # ⭐ If you want only binary digits (without 0b)
# num = int(input("Enter a decimal number: "))

# binary = bin(num)[2:]

# print("Binary:", binary)




# Write a Python program to convert a binary number into decimal using a predefined function.
binary = input("Enter a binary number: ")

decimal = int(binary, 2)

print("Decimal:", decimal)