#list in python,
items = ["apple", "banana", "cherry", "date"]

print(items) 
print(items[-1])

items.pop() # removes the last item
print(items)

items.pop(0) # removes the first item

items.append("lemon") # adds items to the end of the list

print(items)

items[0] = "orange" # changes the first item

print(items)

items = ["apple", "banana", "cherry", "date"]

print(items[0::2])# prints every second item starting from index 0)

items = ["apple", "banana", "cherry", "date"]

print(len(items)) #print the length of the list

items = [0,5,4,8,7,6,10,12,15,20,25,26,23,30,28,35]
print(sorted(items)) #sorts the list in ascending order
print(sorted(items, reverse=True)) #sorts the list in descending order
