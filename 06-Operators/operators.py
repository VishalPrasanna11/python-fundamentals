# Arithmetic Operators
x = 5
y = 2

print(f"Addition: x + y = {x + y}")  # Output: 7   (Adding 5 and 2)
print(f"Subtraction: x - y = {x - y}")  # Output: 3   (Subtracting 2 from 5)
print(f"Multiplication: x * y = {x * y}")  # Output: 10  (Multiplying 5 and 2)
print(f"Division: x / y = {x / y}")  # Output: 2.5 (Dividing 5 by 2)
print(f"Floor Division: x // y = {x // y}")  # Output: 2   (Floor division of 5 by 2)
print(f"Modulus: x % y = {x % y}")  # Output: 1   (Remainder when 5 is divided by 2)
print(f"Exponentiation: x ** y = {x ** y}")  # Output: 25  (5 raised to the power of 2)

# Comparison Operators
x = 5
y = 2

print(f"Is x equal to y? {x == y}")  # Output: False (5 is not equal to 2)

print(f"Is x not equal to y? {x != y}")  # Output: True (5 is not equal to 2)

print(f"Is x greater than y? {x > y}")  # Output: True (5 is greater than 2)

print(f"Is x less than y? {x < y}")  # Output: False (5 is not less than 2)

print(f"Is x greater than or equal to y? {x >= y}")  # Output: True (5 is greater than 2)

print(f"Is x less than or equal to y? {x <= y}")  # Output: False (5 is not less than 2)

# Logical Operators

x = 5
y = 2

print(f"Logical AND: x > 3 and x < 10 = {x > 3 and x < 10}")  # Output: True (5 is greater than 3 and less than 10)

print(f"Logical OR: x > 3 or x < 2 = {x > 3 or x < 2}")  # Output: True (5 is greater than 3)

print(f"Logical NOT: not(x > 3 and x < 10) = {not(x > 3 and x < 10)}")  # Output: False (5 is greater than 3 and less than 10)

# Identity Operators

x = ["apple", "banana"]
y = ["apple", "banana"]

print(f"Is x the same as y? {x is y}")  # Output: False (x and y are two different lists)

print(f"Is x not the same as y? {x is not y}")  # Output: True (x and y are two different lists)

# Membership Operators

x = ["apple", "banana"]

print(f"Is 'banana' in x? {'banana' in x}")  # Output: True ('banana' is present in the list x)

print(f"Is 'pineapple' not in x? {'pineapple' not in x}")  # Output: True ('pineapple' is not present in the list x)

# Bitwise Operators

x = 10  # Binary: 1010
y = 4  # Binary: 0100

print(f"Bitwise AND: x & y = {x & y}")  # Output: 0 (Bitwise AND of 10 and 4)
print(f"Bitwise OR: x | y = {x | y}")  # Output: 14 (Bitwise OR of 10 and 4)
print(f"Bitwise XOR: x ^ y = {x ^ y}")  # Output: 14 (Bitwise XOR of 10 and 4)
print(f"Bitwise NOT: ~x = {~x}")  # Output: -11 (Bitwise NOT of 10)
print(f"Bitwise Left Shift: x << 2 = {x << 2}")  # Output: 40 (Left shift by two bits)
print(f"Bitwise Right Shift: x >> 2 = {x >> 2}")  # Output: 2 (Right shift by two bits)

# Assignment Operators

x = 5

x += 3  # x = x + 3
print(f"x += 3: {x}")  # Output: 8

x -= 3  # x = x - 3
print(f"x -= 3: {x}")  # Output: 5

x *= 3  # x = x * 3
print(f"x *= 3: {x}")  # Output: 15

x /= 3  # x = x / 3
print(f"x /= 3: {x}")  # Output: 5.0

x //= 3  # x = x // 3
print(f"x //= 3: {x}")  # Output: 1

x %= 3  # x = x % 3
print(f"x %= 3: {x}")  # Output: 1

x **= 3  # x = x ** 3
print(f"x **= 3: {x}")  # Output: 1




