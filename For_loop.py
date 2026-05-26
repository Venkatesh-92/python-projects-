for i in range(1,11):
    print(i)
    
for i in range(1,11):
    print(i, end=" ")
    
    
bag = ["red","yellow","green","blue"]
for ball in bag:
    print(ball)
    
for i in range(1,100,2):
    print(i, end=" ")
    
    
name = "venkatesh"
for letter in name:
    print(letter, end=" ")
    
name = "venkatesh"
for letter in name:
    print(letter*10, end= " ")
    
name = "Venkatesh"
for index, letter in enumerate(name):
    print(letter*(index+1))
    
    
l = [12,1234,145,17,199,10]
for index, num in enumerate(l):
    print(f"{num} is in {index}th index") # formate string.

#using break in a for loop.
cities = ["bangalore","mysuru","hubballi","mangalure"]
for city in cities:
    if city == "hubblli":
        print(f" found {city}!")# formated string
        break
    print(city)

    
    
    
    
cities = ["bangalore","manglore","mysore"]
for city in cities:
    if city == "hubblli":
        print(f" found {city}!")
        break
    print(city)
else:
    print(f" not found {city}!")
    
    
key_on = True
fuel_available = True

if key_on:
    if fuel_available:
        print("Engine started")
    else:
        print("No fuel")
else:
    print("Key is OFF")
    
l = [12,30,17,122]
for num in l:
    print(num)
    if num ==17:
        break
else:
    print("all printed")
    
# FOR LOOP ON A DICTIONARAY
d = {"name": "venktesh","age": 32,"income": 1}
for key, value in d.items():
    print(key," ", value)
    
for i in range(1,11):
    print(f"2x{i}={2*i}")


for i in range(2,21):
    for j in range(1,11):
         print(f"{i}x{j}={i*j}")