# ✅ Creating a List:
# Lists are ordered, mutable, and allow duplicate elements.
# Syntax: [item1, item2, ...]
# Example:
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]

fruits = ["apple", "banana", "mango"]
print(fruits)  # Output: ['apple', 'banana', 'mango']

# 🔸 2. Accessing List Elements:
# Elements can be accessed by their index.
# Syntax: list[index]
# Example:
print(fruits[0])  # Output: 'apple'
print(fruits[2])  # Output: 'mango'

# 🔸 Modifying Elements:
fruits[1] = "orange"
print(fruits)  # ['apple', 'orange', 'mango']

# 🔸 3. List Methods:
# Lists have various built-in methods for manipulation.
# Example:
fruits.append("orange")  # Adds 'orange' to the end of the list
print(fruits)  # Output: ['apple', 'banana', 'mango', 'orange']
fruits.append("grape")         # Add to end
fruits.insert(1, "kiwi")       # Insert at index
print(fruits)  # Output: ['apple', 'kiwi', 'banana', 'mango', 'orange', 'grape']

# 🔸 Removing Elements:
fruits.remove("orange")        # Removes first match
fruits.pop()                   # Removes last item
del fruits[0]                  # Deletes index 0


# 🔸 4. Slicing Lists:
# You can extract a portion of a list using slicing.
# Syntax: list[start:end]
# Example:
print(fruits[1:3])  # Output: ['banana', 'mango']

# 🔸 5. List Length:
# You can find the length of a list using the len() function.
# Example:
print(len(fruits))  # Output: 4

# 🔸 6. List Mutability:
# Lists are mutable, meaning you can change their elements.
# Example:
fruits[2] = "pineapple"  # Replaces 'mango' with 'pineapple'
print(fruits)  # Output: ['apple', 'banana', 'pineapple', 'orange']

# 🔸 7. List Methods (Cont.):
# There are many more list methods, such as:
# list.remove(item): Removes the first occurrence of an item.
# list.pop(index): Removes and returns the item at the given index.
# list.sort(): Sorts the list in ascending order.
# list.reverse(): Reverses the order of the list.
# list.count(item): Returns the number of times an item appears in the list.
# list.extend(iterable): Adds all elements of an iterable to the end of the list.
# list.clear(): Removes all elements from the list.
# list.copy(): Returns a shallow copy of the list.
# list.index(item): Returns the index of the first occurrence of an item.

# ✅ Practice Task 1:
# Create a list of 5 numbers and:

# Add a number to the list

# Remove one element

# Sort the list

# Print only the first 3 elements
# Step 1: Create a list of 5 numbers
numbers = [12, 5, 9, 3, 7]

# Step 2: Add a number to the list
numbers.append(10)

# Step 3: Remove one element (e.g., number 5)
numbers.remove(5)

# Step 4: Sort the list
numbers.sort()

# Step 5: Print the first 3 elements
print("First 3 elements:", numbers[:3])
