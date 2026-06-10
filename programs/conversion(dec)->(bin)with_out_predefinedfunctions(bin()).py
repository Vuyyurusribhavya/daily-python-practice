# Write a Python program to convert a decimal number to its binary equivalent without using bin().
a=int(input("Enter a decimal number: "))
binary = ""
while a>0:
    rem=a%2
    print("rem :",rem)
    binary=binary+str(rem)
    a=a//2
print(f"0b{binary}")


