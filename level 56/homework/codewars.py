# 1) თავიდან შეასრულეთ გაკვეთილზე შესრულებული ამოცანები:
# Find the first non-consecutive number
def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
    return None



# altERnaTIng cAsE <=> ALTerNAtiNG CaSe
def to_alternating_case(string):
    return string.swapcase()



# Correct the mistakes of the character recognition software
def correct(s):
    s = s.replace('5', 'S')
    s = s.replace('0', 'O')
    s = s.replace('1', 'I')
    return s



# Is it a palindrome?
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]



# Do I get a bonus?
def bonus_time(salary, bonus):
    if bonus:
        return f"${salary * 10}"
    else:
        return f"${salary}"



# Student's Final Grade
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0



# Sum The Strings
def sum_str(a, b):
    a = int(a) if a else 0
    b = int(b) if b else 0
    return str(a + b)

# Expressions Matter
def expression_matter(a, b, c):
    combs = [
        a+b+c,
        a*b*c,
        (a+b)*c,
        a*(b+c),
        a+(b*c),
        (a*b)+c,
        a*b+c
    ]
    
    return max(combs)

# I love you, a little , a lot, passionately ... not at all
def how_much_i_love_you(nb_petals):
    num=nb_petals % 6
    if num == 0: return "not at all"
    elif num == 1: return "I love you"
    elif num == 2: return "a little"
    elif num == 3: return "a lot"
    elif num == 4: return "passionately"
    elif num == 5: return "madly"

# Count Odd Numbers below n
def odd_count(n):
    return n//2

# Difference of Volumes of Cuboids
def find_difference(a, b):
    v_a = a[0] * a[1] * a[2]
    v_b = b[0] * b[1] * b[2]
    
    if v_a > v_b: return v_a - v_b
    return v_b - v_a

# Welcome!
def greet(language):
    all_lang = [ ("english", "Welcome")
        , ("czech", "Vitejte")
        , ("danish", "Velkomst")
        , ("dutch", "Welkom")
        , ("estonian", "Tere tulemast")
        , ("finnish", "Tervetuloa")
        , ("flemish", "Welgekomen")
        , ("french", "Bienvenue")
        , ("german", "Willkommen")
        , ("irish", "Failte")
        , ("italian", "Benvenuto")
        , ("latvian", "Gaidits")
        , ("lithuanian", "Laukiamas")
        , ("polish", "Witamy")
        , ("spanish", "Bienvenido")
        , ("swedish", "Valkommen")
        , ("welsh", "Croeso")
        ]    
    for key in all_lang:
        if key[0] == language: return key[1]
    
    return "Welcome"

# Drink about
def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"
    
    # Sort and Star
def two_sort(array):
    array.sort()
    
    res = ""
    for i in array[0]:
        res += i+"***"
    
    return res[:-3]

# Short Long Short
def solution(a, b):
    if len(a) > len(b):
        return b+a+b
    else:
        return a+b+a

# My head is at the wrong end!
def fix_the_meerkat(arr):
    arr.reverse()
    return arr

# # 2) Print your name
# # Task: Write a program that prints your full name.
# print("nika samkharadze")

# # 3) Print a favorite quote
# # Task: Print your favorite quote, including quotation marks.
# print("'rest in the end,not in the middle'")

# # 4) Print multiple lines
# # Task: Use the print() function to display a short poem or 3-line message, with each line printed separately.
# print("რომელმან შექმნა სამყარო ძალითა მით ძლიერითა,"
# "ზეგარდმო არსნი სულითა ყვნა ზეცით მონაბერითა,"
# "ჩვენ, კაცთა, მოგვცა ქვეყანა, გვაქვს უთვალავი ფერითა,")
# # 5) Print a simple math result
# # Task: Print the result of a simple addition, like 2 + 3, using print().
# print(2 + 3)
# # 6) Print a shape with symbols
# # Task: Use print() to draw a simple shape, like a triangle or square, using * or #.
# print("   *   ")
# print("  ***  ")
# print(" ***** ")
# # 7) Convert string to integer
# # Task: Create a variable with a numeric string (e.g., "42"), convert it to an integer, and print the result.
# numeric_string = "42"
# print(int(numeric_string))
# # 8) Add two floats
# # Task: Create two float variables (e.g., 3.5 and 2.5), add them together, and print the result.
# float1 = 3.5
# float2 = 2.5
# num_floats = float1 + float2
# print(num_floats)
# # 9) Concatenate two strings
# # Task: Create two str variables (e.g., "Hello" and "World"), join them with a space in between, and print the result.
# str1 = "Hello"
# str2 = "World"
# print(str1 + " " + str2)

# # 10) Print data types
# # Task: Create one variable each of type int, str, and float, and use the type() function with print() to show their data types.
# int1 = 5
# string1 = "nika"
# float3 = 5.4
# print(f"int1- {type(int1)}")
# print(f"string1- {type(string1)}")
# print(f"float3- {type(float3)}")
# # 11) User input and type conversion
# # Task: Ask the user for their age using input(), convert it to an integer, add 1, and print their age next year.
# age = int(input("Enter your age: "))
# next_year = age + 1
# print(f"your age next year will be {next_year}")
# # 12) Ask for your name
# # Task: Write a program that asks the user for their name and prints a greeting, like "Hello, [name]!".
# name = input("enter your name: ")
# print(f"Hello, {name}")
# # 13) Ask for age and calculate next year’s age
# # Task: Ask the user for their age and then print how old they will be next year.
# age = int(input("Enter your age: "))
# next_year = age + 1
# print(f"your age next year will be {next_year}")
# # 14) Simple calculator: addition
# # Task: Ask the user for two numbers (as input), convert them to integers, and print the sum.
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# print(num1 + num2)
# # 15) Favorite color
# # Task: Ask the user for their favorite color and then print a message like "Your favorite color is [color]!".
# fav_color = input("Enter your favourite color: ")
# print(f"Your favourite color is {fav_color}")
# # 16) Check if the user is tall enough
# # Task: Ask the user for their height (in cm) and check if they are taller than 150 cm. Print an appropriate message based on their height.
# height = int(input("Enter your height in cm: "))
# if height > 150:
#     print("You are tall")
# else:
#     print("you are not tall")
# 17) Print numbers from 1 to 5
# Task: Write a program that uses a for loop to print the numbers from 1 to 5.
for i in range(1 , 5):
    print(i)
# 18) Print each letter of a string
# Task: Create a string (e.g., "Python") and use a for loop to print each letter of the string on a new line.
string2 = "python"
for i in string2:
    print(i)
# 19) Sum of numbers 1 to 10
# Task: Use a for loop to calculate and print the sum of numbers from 1 to 10.
for i in range(1 , 10):
    i += 1
print(i)
# 20) Print a multiplication table (1 to 5)
# Task: Write a for loop to print the multiplication table for the number 2 (i.e., 2x1, 2x2, ..., 2x5).
for i in range(1 , 6):
    print(f"2 x {i} = {2 * i}")
# 21) Task: Use a for loop to print all even numbers between 2 and 20 (inclusive).
for i in range(2 , 21 , 2):
    print(i)
# 22) Print numbers from 1 to 5
# Task: Write a while loop that prints numbers from 1 to 5.
number = 1
while True:
    if number == 5:
        break
    else:
        print(number)
    number += 1
# 23) Sum of numbers 1 to 5
# Task: Use a while loop to calculate and print the sum of numbers from 1 to 5.
total = 0
number = 1

while number <= 5:
    total += number
    number += 1

print("Sum:", total)
# 24) Count down from 10 to 1
# Task: Write a while loop that prints the numbers from 10 down to 1.
num = 10
while num > 0:
    print(num)
    num -= 1
# 25) Print all odd numbers between 1 and 10
# Task: Use a while loop to print all odd numbers between 1 and 10.
num = 1
while num <= 10:
    if num % 2 != 0:
        print(num)
    num += 1
# 26) Ask for user input until they enter "exit"
# Task: Write a while loop that repeatedly asks the user to enter something until they type "exit".
password = "exit"
while True:
    user = input("enter something: ")
    if user == password:
        print("correct")
        break
    else:
        print("try again")

# 27) Print all elements of a list
# Task: Create a list with 3 items and use a loop to print each item in the list.
list1 = ["nika" , 14 , "samkharadze"]
for i in list1:
    print(i)
# 28) Find the length of a list
# Task: Create a list and print the number of elements in the list using the len() function.
list2 = ["nika" , 14 , "samkharadze"]
print(len(list2))
# 29) Access a specific element from the list
# Task: Create a list of numbers and print the second element (index 1) of the list.
list3 = [1,2,3,4,5,6,7,8,9]
print(list3[1])
# 30) Add an element to the list
# Task: Create a list with 3 elements and add one more element to the end of the list. Print the updated list.
list4 = ["nika" , 14 , "samkharadze"]
list4.append("rustavi")
print(list4)
# 31) Remove an element from the list
# Task: Create a list, remove an element using remove(), and print the list after the removal.
list5 = ["nika" , 14 , "samkharadze"]
list5.remove("nika")
print(list5)
# 32) Create a list of squares
# Task: Use a list comprehension to create a list of squares for the numbers 1 through 5 (e.g., [1, 4, 9, 16, 25]).
squares = [i**2 for i in range(1 , 6)]
print(squares)
# 33) Create a list of even numbers
# Task: Use a list comprehension to create a list of even numbers from 2 to 10 (inclusive).
numbers = [1,2,3,4,5,6,7,8,9]
even_nums = [i for i in numbers if i % 2 == 0]
print(even_nums)
# 34) Filter odd numbers from a list
# Task: Given a list of numbers, use a list comprehension to create a new list containing only the odd numbers.
odd_nums = [i for i in numbers if i % 2 != 0]
print(odd_nums)
# 35) Convert a list of strings to uppercase
# Task: Given a list of strings, use a list comprehension to create a new list where each string is converted to uppercase.
list6 = ["n" , "o" , "g" , "d"]
uppercase = [i.upper() for i in list6]
print(uppercase)
# 36) Create a list of numbers squared if they are divisible by 2
# Task: Use a list comprehension to create a list that squares each number in a given list only if the number is divisible by 2.
numbers = [1,2,3,4,5,6,7,8,9]
squared = [i**2 for i in numbers if i % 2 == 0]
print(squared)
# 37) Function to greet a user
# Task: Write a function that takes a user's name as a parameter and prints a greeting, such as "Hello, [name]!".
def greet(name):
    return f"hello {name}"
print(greet("nika"))
# 38) Function to add two numbers
# Task: Write a function that takes two numbers as arguments, adds them together, and returns the sum.
def calculate(num1, num2):
    return num1 + num2

print(calculate(28, 7))
# 39) Function to check if a number is even or odd
# Task: Write a function that takes an integer as input and returns whether it is even or odd.
def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
# 40) Function to calculate the area of a rectangle
# Task: Write a function that takes the length and width of a rectangle as arguments and returns the area.
def area(length, width):
    return length * width
# 41) Function to reverse a string
# Task: Write a function that takes a string as input and returns the string reversed.
def reverse(string):
    return string[::-1]


print(reverse("nika"))
# 42) Create and print a tuple
# Task: Create a tuple with 3 elements (e.g., an integer, a string, and a float) and print the tuple.
tuple1 = (9, "rustavi", 7.5)
print(tuple1)
# 43) Access an element in a tuple
# Task: Create a tuple with several items and print the second element (index 1) of the tuple.
tuple1 = (9, "rustavi", 7.5)
print(tuple1[1])
# 44) Find the length of a tuple
# Task: Create a tuple and use the len() function to print the length of the tuple.
tuple1 = (9, "rustavi", 7.5)
print(len(tuple1))
# 45) Concatenate two tuples
# Task: Create two tuples and use the + operator to concatenate them, then print the result.
tuple1 = (9, "rustavi", 7.5)
tuple2 = ("goa", "hello", "c")
result = tuple1 + tuple2
print(result)
# 46) Check if an item exists in a tuple
# Task: Create a tuple and use an if statement to check if a specific element exists in the tuple. Print "Found" if it exists, otherwise print "Not found".
tuple1 = (9, "rustavi", 7.5)
element_to_check = "hello"
if element_to_check in tuple1:
    print("Found")
else:
    print("Not found")
# 47) Create and print a set
# Task: Create a set with 3 different elements (e.g., numbers or strings) and print the set.
set1 = {9, "rustavi", 7.5}
print(set1)
# 48) Check if an element is in a set
# Task: Create a set and use an if statement to check if a specific element is in the set. Print "Yes" if the element is found, otherwise print "No".
if "hello" in set1:
    print("Yes")
else:
    print("No")
# 49) Add an element to a set
# Task: Create a set, add a new element to it using the add() method, and print the updated set.
set1 = {9, "rustavi", 7.5}
set1.add("georgia")
print(set1)
# 50) Remove an element from a set
# Task: Create a set, remove an element using the remove() method, and print the updated set.
set1.remove(9)
print(set1)
# 51) Find the union of two sets
# Task: Create two sets and use the | operator to find their union, then print the result.
set2 = {1, 2, 3}
set3 = {3, 4, 5}
union_set = set2 | set3
print(union_set)
# 52) Create and print a dictionary
# Task: Create a dictionary with at least two key-value pairs (e.g., name and age), and print the dictionary.
dict1 = {
    "name":"nika",
    "age": 14
}
print(dict1)
# 53) Access a value by key
# Task: Given a dictionary, access and print the value associated with a specific key.
dict1 = {
    "name":"nika",
    "age": 14
}
print(dict1["name"])
# 54) Add a new key-value pair to a dictionary
# Task: Create a dictionary and add a new key-value pair to it. Print the updated dictionary.
dict1 = {
    "name":"nika",
    "age": 14
}
dict1["city"] = "rustavi"
print(dict1)

# Basic variable assignment
a = "code"
b = "wa.rs"
name = a + b

# get character from ASCII Value
def get_char(c):
    return chr(c)