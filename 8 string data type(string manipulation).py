first_name ="venkatesh"
last_name = "uv"
full_name = first_name + " " + last_name
print(full_name)

# repetition
message = "this is a warning!  "
print(message)

print(message*10)

print(message.upper())

print(message.lower())

print(message.strip()*10)

print(message.replace("warning", "error"))

name = "venkatesh said 'hello' "
print(name)

name = '''venkatesh going to "school"
             deepu going to "america"
              some one going to "collage"
                 ganesh going to "shopping"
                     bharath going to "vocation"
                         nandish getting married on "december"
'''
print(name)

name = "venkateshdeepu"# (index = position -1),(position = index +1) position will start from 1 & index will start from 0
print(name[13]) 

# slicing strings
name = "venkatesh"
print(name[2:6])
print(name[:3])
print(name[2:])

name = "venkatesh"
print(name[3])
print(name[-6 ])

name = "venkatesh"
print(name[::4]) # print every 4th character

# escape_sequence
name = "venkatesh is a good boy\nvenkatesh is a good student"
print(name)

name = "venkatesh is a good boy\t     venkatesh is a good student"
print(name)

name = "venkatesh is a good boy\\ venkatesh is a good student"
print(name)