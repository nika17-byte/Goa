# 1) Function 1 - hello world
def greet():
    return "hello world!"

# 2) Counting sheep...
def count_sheeps(sheep):
    return sheep.count(True)

# 3) Remove String Spaces
def no_space(x):
    return x.replace(" ", "")

# 4) You Can't Code Under Pressure #1
def double_integer(i):
    return i*2

# 5) Returning Strings
def greet(name):
    return f"Hello, {name} how are you doing today?"

# 6) Convert a Boolean to a String
def boolean_to_string(b):
    return str(b)

# 7) Basic Mathematical Operations
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "":
        return value1 * value2
    else:
        return value1 / value2

# 8) Keep Hydrated!
def litres(time):
    return time // 2

# 9) Century From Year
def century(year): 
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

# 10) Convert number to reversed array of digits
def digitize(n):
    starting_str = str(n)
    reversed_str = starting_str[::-1]

    res_list = []

    for i in reversed_str:
        res_list.append(int(i))

    return res_list

# 11) Beginner - Lost Without a Map
def maps(a):
    saver=[]
    for i in a:
        saver.append(i*2)
    return saver

# 12) Opposites Attract
def lovefunc( flower1, flower2 ):
    return (flower1 + flower2)%2 == 1

def sum_array(a):
    return sum(a)

def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    return n * m

def make_upper_case(s):
    return s.upper()

def past(h, m, s):
    return (h * 3600 + m * 60 + s) * 1000

def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    
def abbrev_name(name):
    initials = name.split()
    return f"{initials[0][0].upper()}.{initials[1][0].upper()}"