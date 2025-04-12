# საკლასო დავალება:

# Task: Division Calculator with Error Handling

# Ask the user to input two numbers: a numerator and a denominator.

# Attempt to divide the numerator by the denominator inside a try block.

# If the user inputs something that is not a number, catch the error and display a message using except.

# If the user attempts to divide by zero, raise a ValueError with a custom message.

# Regardless of what happens, use a finally block to print a message like “Operation complete.”
try:
    numerator = float(input("enter numerator (numerator): "))
    denominator = float(input("enter denominator (denominator): "))

    if denominator == 0:
        raise ValueError("you cant number divide by 0!")

    result = numerator / denominator
    print("result:", result)

except ValueError as error:
    print("error:", error)

finally:
    print("operation is done")

# საკლასო დავალება:

# Write a function apply_to_list(func, values) that takes a function func and a list values, and returns a new list where func is applied to each element.

# Then:

# Define a function square(x) that returns the square of a number.
def square(i):
    return i * i

def apply_to_list(func, values):
    return [func(value) for value in values]

values = [1, 2, 3, 4, 5]
result = apply_to_list(square, values)
print(result)