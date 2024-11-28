# Creating a set
my_set = {1, 2, 3, 4}

# Adding elements
my_set.add(5)

# Removing elements
my_set.remove(2)  # Removes 2 (raises KeyError if not found)
my_set.discard(6)  # Removes 6 (does nothing if not found)

# Set operations

another_set = {3, 4, 5, 6}
print("another_set:", another_set)
union_set = my_set.union(another_set)  # Union of two sets
intersection_set = my_set.intersection(another_set)  # Intersection of two sets

# Printing the set and results
print("my_set",my_set)  # Output: {1, 3, 4, 5}
print("Union:", union_set)  # Output: {1, 3, 4, 5, 6}
print("Intersection:", intersection_set)  # Output: {3, 4, 5}
