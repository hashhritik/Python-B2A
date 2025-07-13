# 🔹 1. for Loop
# a) Looping through a range:
for i in range(5):
    print(i)
# Output: 0 1 2 3 4

# b) Looping through a list:
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
# Output: apple banana mango

# 🔹 2. while Loop
i = 0
while i < 5:
    print(i)
    i += 1
# Output: 0 1 2 3 4

# 🔹 3. break and continue    
# break: Exits the loop completely.
for i in range(10):
    if i == 5:
        break
    print(i)
# Output: 0 1 2 3 4 5 6 7 8 9

# b) continue: Skips current iteration.
for i in range(5):
    if i == 2:
        continue
    print(i)
# Output: 0 1 3 4

# 🔹 4. else with Loops
for i in range(3):
    print(i)
else:
    print("Loop completed")
# Output: 0 1 2 Loop completed


# Taking input from user
n = int(input("Enter a number: "))

# Loop from 1 to n
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
