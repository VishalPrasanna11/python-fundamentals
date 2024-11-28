# Creating a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Accessing values
print(my_dict["name"])  # Output: Alice

# Adding or modifying values
my_dict["age"] = 26  # Modifies the existing key "age"
my_dict["job"] = "Engineer"  # Adds a new key-value pair

# Removing elements
del my_dict["city"]  # Removes the key "city"
popped_value = my_dict.pop("job")  # Removes and returns the value of "job"

# Printing the dictionary
print(my_dict)  # Output: {'name': 'Alice', 'age': 26}
print(f"Popped Value: {popped_value}")  # Output: Engineer



#Example Frequency Count
# Array of numbers
numbers = [1, 2, 2, 3, 4, 5, 3, 2, 1, 3, 4, 4, 4]

# Initialize an empty dictionary for frequency count
frequency = {}

# Count frequencies
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Print the frequency count
print(frequency)  # Output: {1: 2, 2: 3, 3: 3, 4: 4, 5: 1}
