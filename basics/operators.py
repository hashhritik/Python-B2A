a = 10
b = 3

print(a + b)   # Addition → 13
print(a - b)   # Subtraction → 7
print(a * b)   # Multiplication → 30
print(a / b)   # Division → 3.333...
print(a // b)  # Floor Division → 3
print(a % b)   # Modulus → 1 (remainder)
print(a ** b)  # Exponentiation → 1000


a = 5
b = 10

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True

x = 5
print(x > 3 and x < 10)  # True (both conditions are True)
print(x > 3 or x < 4)    # True (at least one is True)
print(not(x > 3))        # False (not True → False)

x = 5       # Simple assignment
x += 3      # x = x + 3 → 8
x -= 2      # x = x - 2 → 6
x *= 2      # x = x * 2 → 12
x /= 3      # x = x / 3 → 4.0
x %= 3      # x = x % 3 → 1
x **= 2     # x = x ** 2 → 1

# Identity Operators
print(a is b)  # False (a and b have different values)
print(a is not b)  # True (a and b have different values)


# Bitwise Operators
a = 10  # Binary: 1010
b = 3   # Binary: 0011

print(a & b)  # Bitwise AND → 0010 (Binary) → 2
print(a | b)  # Bitwise OR → 1011 (Binary) → 11
print(a ^ b)  # Bitwise XOR → 1001 (Binary) → 9
print(~a)    # Bitwise NOT → 11111111111111111111111111111010 (Binary) → -11
print(b << 1)  # Bitwise Left Shift → 0110 (Binary) → 6
print(b >> 1)  # Bitwise Right Shift → 0001 (Binary) → 1
print(a >> 1)  # Bitwise Right Shift → 0101 (Binary) → 5
print(a << 1)  # Bitwise Left Shift → 10100 (Binary) → 20


a = 5        # In binary: 0101
b = 3        # In binary: 0011

print(a & b)   # 1 → 0001 (only last bit is 1 in both)
print(a | b)   # 7 → 0111
print(a ^ b)   # 6 → 0110 (XOR: different bits = 1)
print(~a)      # -6 → Inverts all bits (2's complement)
print(a << 1)  # 10 → 1010 (shift left by 1)
print(a >> 1)  # 2 → 0010 (shift right by 1)

a = 5     # ~a in Python, it returns -(a + 1) 
print(~a)  # -6

x = 6  # binary: 0110
y = 2  # binary: 0010

print("AND:", x & y)
print("OR:", x | y)
print("XOR:", x ^ y)
print("NOT x:", ~x)
print("x << 2:", x << 2)
print("x >> 1:", x >> 1)


x = 6  # binary: 0110
y = 2  # binary: 0010

print("AND:", x & y)
print("OR:", x | y)
print("XOR:", x ^ y)
print("NOT x:", ~x)
print("x << 2:", x << 2)
print("x >> 1:", x >> 1)




# Take input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Binary representations
print(f"\nBinary of {a}: {bin(a)}")
print(f"Binary of {b}: {bin(b)}")

# Bitwise operations
print(f"\nAND: {a & b}")
print(f"OR: {a | b}")
print(f"XOR: {a ^ b}")
print(f"NOT of {a}: {~a}")

# Bit shifting
print(f"{a} << 2: {a << 2}")
print(f"{b} >> 1: {b >> 1}")

#Use bin(), oct(), or hex() functions to view binary, octal, and hexadecimal formats of numbers.
print(f"\nOctal of {a}: {oct(a)}")
print(f"Octal of {b}: {oct(b)}")
print(f"\nHexadecimal of {a}: {hex(a)}")
print(f"Hexadecimal of {b}: {hex(b)}")
