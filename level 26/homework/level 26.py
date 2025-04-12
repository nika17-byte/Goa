# 2) Sum of Two Numbers: Write a function that takes two numbers as input and returns their sum.
a = int(input("Enter number: "))
b = int(input("Enter number: "))
def sum_numbers(a,b):
    print(a + b)
print("The sum of",a ,"and",b , "is", a + b)
# 3) Even or Odd: Create a function that determines whether a given integer is even or odd.
x = int(input("Enter number: "))
def even_odd(x):
    if x % 2 == 0:
        print(x,"is even number")
    elif x % 2 != 0:
        print(x,"is odd number")
# 4) Reverse a String: Implement a function that takes a string and returns it reversed.
y = str(input("Enter word: "))
def reverse_string(y):
    print(y[::-1])
print("the reversed word is", y[::-1])
# 5) Find Maximum: Create a function that takes a list of numbers and returns the maximum value.
def find_max(num_list):
    max_value = num_list[0]

    for num in num_list:
        if num > max_value:
            max_value = num

    print(max_value)

find_max([1 , 4 , 2 , 3 , 10 , 3 , 5])
# 6) Factorial: Implement a function to calculate the factorial of a given number.
def factorial(num):
    result = 1

    for i in range(2, num + 1):result *= i

    print(result)

    factorial(5)