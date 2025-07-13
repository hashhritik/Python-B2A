 # 🔸 2. Creating Tuples:
# Tuples are ordered, immutable, and allow duplicate elements.
# Syntax: (item1, item2, ...)
# Example:
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

# 🔸 3. Accessing Elements:
# You can access tuple elements using indexing and slicing.
# Example:
print(my_tuple[0])  # Output: 1
print(my_tuple[2:4])  # Output: (3, 4)

# 🔸 4. Tuple Methods:
# Tuples have two built-in methods:
# count(item): Returns the number of times a specific value occurs in a tuple
# index(item): Searches the tuple for a specified value and returns the first position of the match
# Example:
print(my_tuple.count(2))  # Output: 1
print(my_tuple.index(4))  # Output: 3

# 🔸 5. Immutability:
# Tuples are immutable, meaning their elements cannot be changed.
# Example:
# my_tuple[0] = 10  # This will raise an error

# 🔸 6. Packing and Unpacking:
# You can create tuples without parentheses.
# Example:
my_tuple = 1, 2, 3
print(my_tuple)  # Output: (1, 2, 3)

# You can unpack tuples into variables.
# Example:
a, b, c = my_tuple
print(a, b, c)  # Output: 1 2 3


 
# 🔸 7. Tuple Operations:
# You can perform operations on tuples, such as concatenation and repetition.
# Example:
tuple1 = (1, 2)
tuple2 = (3, 4)
print(tuple1 + tuple2)  # Output: (1, 2, 3, 4)

# 🔸 8. Nested Tuples:
# You can create tuples within tuples.
# Example:
nested_tuple = (1, 2, (3, 4))
print(nested_tuple)  # Output: (1, 2, (3, 4))
print(nested_tuple[2])  # Output: (3, 4)

# 🔸 9. Tuple Length:
# You can use the len() function to get the length of a tuple.
# Example:
print(len(my_tuple))  # Output: 3

# 🔸 10. Tuple Membership:
# You can check if an item is in a tuple using the 'in' keyword.
# Example:
print(3 in my_tuple)  # Output: True

# 🔸 11. Tuple Iteration:
# You can loop through a tuple using a 'for' loop.
# Example:
for item in my_tuple:
    print(item)  # Output: 1 2 3 4 5

# 🔸 12. Tuple Comparison:
# You can compare tuples using comparison operators (e.g., ==, !=, <, >, etc.).
# Example:
tuple3 = (1, 2, 3)
tuple4 = (1, 2, 4)
print(tuple3 == tuple4)  # Output: False

# 🔸 13. Tuple Conversion:
# You can convert other data types to tuples using the tuple() function.
# Example:
list1 = [1, 2, 3]
tuple_from_list = tuple(list1)
print(tuple_from_list)  # Output: (1, 2, 3)


# 🔸 14. Tuple Destructuring:
# You can unpack a tuple into multiple variables.
# Example:
a, b, c, d = my_tuple
print(a, b, c, d)  # Output: 1 2 3 4 5

# 🔸 15. Summary:
# Tuples are ordered, immutable, and allow duplicate elements.
# You can access tuple elements using indexing and slicing.
# You can perform operations on tuples, such as concatenation and repetition.
# You can convert other data types to tuples using the tuple() function.
# You can unpack a tuple into multiple variables using tuple destructuring.
# You can check if an item is in a tuple using the 'in' keyword.
# You can get the length of a tuple using the len() function.
# You can loop through a tuple using a 'for' loop.
# You can compare tuples using comparison operators (e.g., ==, !=, <, >, etc.).
# You can create tuples without parentheses.
# You can use tuples as keys in dictionaries.
# You can use tuples as values in sets.
# You can use tuples as return values from functions.
# You can use tuples to store multiple values in a single variable.

# ✅ Practice Task 2:
# Create a tuple of 4 names:

# Print the second name

# Count how many times a specific name appears

# Find the index of a given name
# Step 1: Create a tuple of 4 names
names = ("Hritik", "Ravi", "Aman", "Ravi")

# Step 2: Print the second name (index 1)
print("Second name:", names[1])

# Step 3: Count how many times "Ravi" appears
print("Occurrences of 'Ravi':", names.count("Ravi"))

# Step 4: Find the index of "Aman"
print("Index of 'Aman':", names.index("Aman"))


# 🔸 16. Conclusion:
# In this chapter, you learned about tuples, which are ordered, immutable, and allow duplicate elements.
# You learned how to create, access, and manipulate tuples, as well as how to use tuples in loops, comparisons, and other operations.
# You also learned about tuple destructuring and how to use tuples as keys and values in dictionaries and sets.
# In the next chapter, we will learn about sets.
