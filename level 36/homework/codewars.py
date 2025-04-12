def find_smallest_int(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

def string_to_number(s):
    return int(s)

def summation(num):
    result = sum(range(1 , num + 1))
    if num > 0:
        return result
    else:
        return "Wrong number"
    
def open_or_senior(data):
    result = []
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result
    
def get_sum(a,b):
    if a != b:
        return a + b
    else:
        return a or b

def get_sum(a,b):
    total = 0
    start, end = min(a, b), max(a, b)
    for num in range(start, end + 1):
        total += num
    return total

def accum(st):
    result = ""
    for i, char in enumerate(st):
        part = char.upper() + char.lower() * i
        if i > 0:
            result += "-" + part
        else:
            result += part
    return result

def count_bits(n):
    return bin(n).count('1')
    number = int(input("Enter an integer: "))
    print("Number of 1 bits:", count_bits(number))

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"
    
def greet():
    return "hello world!"
greet()

def count_sheeps(sheep):
    return sheep.count(True)

def no_space(x):
    return x.replace(" ","")

def double_integer(i):
    return i * 2

def greet(name):
    return f"Hello, {name} how are you doing today?"

def boolean_to_string(b):
    return str(b)

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        if value2 != 0:
            return value1 / value2
        else:
            return "Division by zero"
    else:
        return "Invalid operator"
    
def litres(time):
    return time // 2

def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return (year // 100) + 1

def maps(a):
    return [i * 2 for i in a]

def digitize(n):
    return [int(digit) for digit in str(n)[::-1]]

def lovefunc( flower1, flower2 ):
    return (flower1 % 2 != flower2 % 2)

def sum_array(a):
    if a != 0:
        return sum(a)
    elif a == 0:
        return "0"