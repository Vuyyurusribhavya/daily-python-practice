# Write a Python program to convert a binary number into its decimal equivalent without using predefined functions such as int(binary, 2).
binary = "0b10"

# Remove the '0b' prefix
binary = binary[2:]

decimal = 0
power = 0

for digit in binary[::-1]:
    decimal += (ord(digit) - ord('0')) * (2 ** power)
    power += 1

print(decimal)


