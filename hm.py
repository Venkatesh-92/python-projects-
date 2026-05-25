# Take a sentence as input from the user
sentence = input("Enter a sentence: ")

# Remove leading and trailing white spaces
sentence = sentence.strip()

# Print the sentence in uppercase
print("Uppercase:", sentence.upper())

# Print the sentence in lowercase
print("Lowercase:", sentence.lower())

# Replace all spaces with underscores
print("Replaced spaces:", sentence.replace(" ", "_"))
