# assinment operators,
a = 10
a += 100 #a = a + 100
print(a)


a = 10
a -= 100 #a = a - 100
print(a)

a = 10
a *= 100 #a = a * 100
print(a)


a = 10
a /= 100 #a = a / 100
print(a)

#comparison operators,
a = 10
b = 20

print(a == b) # output will be boolean value: False
print(a != b) # output will be boolean value: True
print(a > b)  # output will be boolean value: False
print(a < b)  # output will be boolean value: True
print(a >= b) # output will be boolean value: False
print(a <= b) # output will be boolean value: True

# logocal operators,
print(1>2 and 1<2)
print(1>2 or 1<2)
print(not(1>2))

# membership operators,
S = "Venkatesh"
print("V" in S)

S = "Venkatesh"
print("Z" in S) 
 # or
print("z" not in S)

# bitwise operators,
a = 5 # Binary: 1010
b = 3  # Binary: 0010
print(a & b)  #bitwise AND # O/P:1(Binary: 0001)
print(a | b)  #bitwise OR  # O/P:7(Binary: 0111)
print(a ^ b)  #bitwise XOR # O/P:6(Binary: 0110)
print(~a)     #bitwise NOT #O/P:-6( Invertes all bits)
print(a << 1) #bitwise left shift # O/P:10(Binary: 1010)
print(a >> 1) #bitwise right shift # O/P:2(Binary: 0010)
