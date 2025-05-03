def get_char(c):
    return chr(c)

# Exclusive "or" (xor) Logical Operator
def xor(a,b):
    return a!= b

# What's the real floor?
def get_real_floor(n):
    if n < 1:
        return n
    elif n < 13:
        return n-1
    elif n > 13:
        return n-2
# Filter out the geese
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]
# Name Shuffler
def name_shuffler(s):
    parts = s.split()
    return f"{parts[1]} {parts[0]}"
# Find numbers which are divisible by given number
def divisible_by(numbers, divisor):
    return [num for num in numbers if num % divisor == 0]
# Lario and Muigi Pipe Problem
def pipe_fix(nums):
    return list(range(min(nums), max(nums) + 1))
# Plural
def plural(n):
    return n == 0 or n > 1
# Multiplication table for number
def multi_table(number):
    res = ""
    for i in range(1,11):
        res += f"{i} * {number} = {i*number}\n"
    return res[0:-1]
# Super Duper Easy
def problem(a):
    if type(a) == str: return "Error"
    return a*50+6
# Grasshopper - If/else syntax debug
def check_alive(health):
    if health > 0:
        return True
    else:
        return False
# Grasshopper - Basic Function Fixer
def add_five(num):
    total = num + 5
    return total
# Grasshopper - Terminal game combat function
def combat(health, damage):
    if health - damage > 0: return health - damage
    return 0
# საკლასო დავალება:
# https://www.codewars.com/kata/595970246c9b8fa0a8000086
def capitalize_word (word : str) -> str:
    return word.capitalize()
# How many lightsabers do you own?
def how_many_light_sabers_do_you_own(*args):
    if len(args) == 0: return 0
    return 18 if args[0] == "Zach" else 0
# საკლასო დავალება:
# https://www.codewars.com/kata/563b74ddd19a3ad462000054
def stringy(size):
    result = ""
    for i in range(size):
        if i % 2 == 0:
            result += "1"
        else:
            result += "0" 
    return result
# Remove duplicates from list
def distinct(seq):
    res = []

    for i in seq:
        if i not in res: res.append(i)

    return res
# საკლასო დავალება:
# https://www.codewars.com/kata/5899642f6e1b25935d000161
def merge_arrays(arr1, arr2):
    return sorted(list(set(arr1+arr2)))