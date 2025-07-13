# 🔹 1. Defining a Function
def greet():
    print("Hello, Hritik!")

# 🔹 2. Function with Parameters
def greet(name):
    print(f"Hello, {name}!")
    
greet("Hritik")

# 🔹 3. Function with Return Value
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8

# 🔹 4. Default Parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Hello, Guest
greet("Hritik")  # Hello, Hritik

# 🔹 5. Keyword Arguments
def intro(name, age):
    print(f"My name is {name} and I am {age} years old.")

intro(age=22, name="Hritik")


# 🔹 6. Arbitrary Arguments
# a) *args – Multiple positional arguments:
def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3, 4))  # Output: 10

# b) **kwargs – Multiple keyword arguments:
def user_info(**details):
    print(details)

user_info(name="Hritik", age=22)



# ✅ Practice Task
# Write a function named check_even_odd(n) that:

# Takes a number n

# Prints "Even" if it’s even

# Prints "Odd" if it’s odd

# 🧾 Sample Output:
# Enter a number: 7
# Odd

# Define the function
def check_even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

# Get input from user
number = int(input("Enter a number: "))

# Call the function
check_even_odd(number)
