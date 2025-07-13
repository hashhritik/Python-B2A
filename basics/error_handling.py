# 🔸 1. Basic Try-Except Block
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter a valid number.")

# 🔸 2. Catching Any Error (Generic Exception)
try:
    # risky code
    pass
except Exception as e:
    print("Something went wrong:", e)

# 🔸 3. else and finally in Error Handling
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Divide by zero error!")
else:
    print("No error occurred:", result)
finally:
    print("This block always runs.")


# 🔸 4. Raising Your Own Errors
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print(f"Your age is {age}")

set_age(-1)  # Will raise an error


# 🔸 5. Creating Custom Exceptions (Advanced)
class TooSmallError(Exception):
    pass

def check_number(n):
    if n < 10:
        raise TooSmallError("Number is too small!")

try:
    check_number(5)
except TooSmallError as e:
    print(e)


# 🔸 6. Logging Instead of Printing Errors
import logging

logging.basicConfig(level=logging.ERROR)

try:
    a = 1 / 0
except ZeroDivisionError as e:
    logging.error("Tried dividing by zero!", exc_info=True)



# ✅ Practice Task
# Create a program that:

# Asks the user to enter two numbers

# Divides them

# Handles:

# Invalid input (ValueError)

# Division by zero (ZeroDivisionError)

# Any unexpected error

# Bonus: Use finally to print “Program ended.”

def divide_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        print("❌ Invalid input! Please enter numeric values only.")
    except ZeroDivisionError:
        print("❌ Cannot divide by zero.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
    else:
        print(f"✅ Result: {result}")
    finally:
        print("🛑 Program ended.")

# Call the function
divide_numbers()
