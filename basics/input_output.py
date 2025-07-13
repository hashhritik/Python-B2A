name = input("Enter your name: ")
print("Hello,", name)
# Note: input() always returns a string. You must convert it if you need numbers.

age = int(input("Enter your age: "))
pi = float(input("Enter the value of pi: "))


print("Hello, World!")


# a) Using , (comma):
name = "Hritik"
age = 22
print("Name:", name, "| Age:", age)

# b) Using + (plus):
print("Name: " + name + " | Age: " + str(age))
# c) Using format() method:
print("Name: {} | Age: {}".format(name, age))
# d) Using f-strings (Python 3.6+):
print(f"Name: {name} | Age: {age}")

# e) Using % formatting (older style):
print("Name: %s | Age: %d" % (name, age))
# f) Using join() and str():
print(" | ".join(["Name:", name, "Age:", str(age)]))
# g) Using * (repeat):
print("Name:", name, "* Age:", age, sep="")
# h) Using write() and read() methods:
with open("output.txt", "w") as file:
    file.write("Name: {} | Age: {}".format(name, age))
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
# i) Using input() and print() methods:
name = input("Enter your name: ")
print("Hello, " + name)
# j) Using readline() and readlines() methods:
with open("input.txt", "w") as file:
    file.write("Line 1\nLine 2\nLine 3")
with open("input.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()
    print(line1, line2, line3)
# k) Using seek() and tell() methods:
with open("input.txt", "r") as file:
    file.seek(0)
    print(file.tell())
    file.seek(6)
    print(file.tell())
    file.seek(0, 2)
    print(file.tell())


# 🔹 3. Customizing print output
# a) end parameter (default is newline \n):
print("Hello", end=" ")
print("World")  # Output: Hello World


# b) sep parameter:
print("2025", "07", "09", sep="-")  # Output: 2025-07-09

# Taking input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
language = input("Enter your favorite language: ")

# Displaying output using f-strings
print(f"\nHi {name}, you're {age} years old and you love {language}!")
