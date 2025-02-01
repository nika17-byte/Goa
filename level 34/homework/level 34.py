from turtle import *
# 2) Function Basics: Write a function that takes no arguments and simply prints "Hello, World!"
def greet():
    print("Hello, World!")
greet()
# 3) Arguments and Parameters: Write a function that takes two numbers as arguments and prints their sum.
def sum_of_numbers(num1 , num2):
    print(num1 + num2)
sum_of_numbers(17 , 34)
# 4) Return Statement: Create a function that takes a number as input, multiplies it by 10, and returns the result.
def multipling_number(num3):
    result = num3 * 10
    return result
# 5) Default Arguments: Define a function that takes a name as input and prints a greeting. If no name is provided, it should use "Guest" as the default.
def greet(name="Guest"):
    print(f"Hello, {name}!")
greet("kai chemi dedas vficavar too") 
greet()
# 6) Boss level: Nested Functions: Define a function that contains another function inside it and calls the inner function.
def outer_function(x):

    def inner_function(y):
        return y * y

    return inner_function(x) + x

result = outer_function(5)
print(result)
# 7) Write a function that takes a list of numbers and checks whether each number is even or odd using a loop and conditional 
# statements. Print "Even" for even numbers and "Odd" for odd numbers.
def check_even_odd(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is Even")
        else:
            print(f"{number} is Odd")

numbers_list = [10, 21, 32, 43, 54, 65]
check_even_odd(numbers_list)
# 8) Find the Maximum
# Create a function that takes a list of numbers and uses a loop to find and return the maximum number.
def find_max(nums):
    for num in nums:
        max_num = max(nums)
    print(f"The maximum number in list is {max_num}")

my_list = [1 , 2 , 3 , 4 , 5 , 6 , 9]
find_max(my_list)
# 9) Define a function that takes a list of integers and returns a new list containing only the positive numbers. Use a loop and a conditional statement.
def filter_positive_numbers(numbers):
    positive_numbers = []

    for number in numbers:
        if number > 0: 
            positive_numbers.append(number)

    return positive_numbers

numbers_list = [-10, 15, -3, 0, 7, 4, -22]
positive_list = filter_positive_numbers(numbers_list)
print(f"The list of positive numbers is: {positive_list}")
# 10) Write a function that iterates through a range of numbers (e.g., 1 to 100) and sums up all the numbers divisible by 3. Return the total sum.
def sum_divisible_by_three(start, end):
    total_sum = 0

    for number in range(start, end + 1):
        if number % 3 == 0:
            total_sum += number  

    return total_sum

result = sum_divisible_by_three(1, 100)
print(f"The sum of numbers divisible by 3 from 1 to 100 is: {result}")