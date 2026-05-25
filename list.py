items = ["apple", "bananna","cherry","date"]
print(items)
print(items[1]) # it is indicate the index of the items 

items = ["apple", "bananna","cherry","date"]
items.pop() # removes the last element.
print(items)

items = ["apple", "bananna","cherry","date"]
items.pop(0) # removes the first element.
print(items)

items = ["apple", "bananna","cherry","date"]
items.append("orange") # adds an element to the list.
print(items)

items = ["apple", "bananna","cherry","date"]
items.remove("bananna") # removes the specific element.
print(items)

items = ["apple", "bananna","cherry","date"]
items.insert(2, "kiwi") # adds an element at specific index.
print(items)