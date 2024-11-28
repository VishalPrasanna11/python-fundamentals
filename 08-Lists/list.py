# Creating a list
my_list = [1, 2, 3, 4]

# Adding elements
my_list.append(5)  # Adds 5 to the end
my_list.insert(1, 6)  # Inserts 6 at index 1

#  1 6 2 3 4 5
# Modifying elements
my_list[0] = 10  # Changes the first element to 10
# 10 6 2 3 4 5
# Removing elements
my_list.remove(3)  # Removes the element with value 3
popped_value = my_list.pop(2)  # Removes and returns the element at index 2
# 10 6 4 5
# Printing the list
print(my_list)  # Output: [10, 6, 4, 5]
print(f"Popped Value: {popped_value}")  # Output: 2
