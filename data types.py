name = "venkatesh" #string
age = 32 #integer
is_married = True #boolean
height = 5.9 #float




print(type("venkatesh"))
print(type(32))
print(type(True))
print(type(5.9))


age = 32
age_float = float(age)
print(age_float)


age = 32
S = "100"
print(int(S)+age)


# "arithmetic operations"
a = 17
b = 67

print(a + b) #o/p: 84
print(a - b) #o/p:-50
print(a * b) #o/p:1139
print(a / b) #o/p:0.2537
print(a // b) #o/p:0 (floor division)
print(a % b) #o/p:17 (modulus|remainder)
print(a ** b) #o/p:27547217140(exponentiation)


# Define two numbers

num1 = 10
num2 = 5

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2

print("number 1:", num1)
print("number 2:", num2)
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)


# Swapping values using a third variable
print("=== Swapping using a third variable ===")
a = 10
b = 20
print("Before swapping: a =", a, ", b =", b)

# Using a temporary variable
temp = a
a = b
b = temp

print("After swapping: a =", a, ", b =", b)

# Swapping values without using a third variable
print("\n=== Swapping without using a third variable ===")
x = 5
y = 15
print("Before swapping: x =", x, ", y =", y)

# Using arithmetic operations
x = x + y
y = x - y
x = x - y

print("After swapping: x =", x, ", y =", y)

# Alternatively, you can use Python's tuple unpacking
print("\n=== Swapping using tuple unpacking (Pythonic way) ===")
p = 7
q = 3
print("Before swapping: p =", p, ", q =", q)
p, q = q, p
print("After swapping: p =", p, ", q =", q)
