

# EX:PROGRAM 4

is_failed = True
i = 1

while is_failed:
    if i%2!=0: #is not even
        i = i + 1
        continue
    print(f"Attempt {i}")
    i = i + 1
    if i>100:
        break
print("I gave up !")

# EX:PROGRAM 5
i = 0