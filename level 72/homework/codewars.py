# You're a square!
def is_square(n):
    if n < 0: return False

    #if int(n0.5)int(n0.5)==n: return True
    return False
# Get the Middle Character
def get_middle(s):
    if len(s)%2 == 0:
        return s[len(s)//2-1:len(s)//2+1]
    else:
        return s[len(s)//2]
# Isograms
def is_isogram(string):
    string = string.lower()
    return len(string) == len(set(string))
# Exes and Ohs
def xo(s):
    s = s.lower()
    return s.count("o") == s.count("x")
# Jaden Casing Strings
def to_jaden_case(string):
    string = [i.capitalize() for i in string.split(" ")]
    return " ".join(string)

# საკლასო დავალება:

# შეასრულეთ ამოცანა:

# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
def accum(st):
    result = ""
    for i, char in enumerate(st):
        part = char.upper() + char.lower() * i
        if i > 0:
            result += "-" + part
        else:
            result += part
    return result

#Sum of two lowest positive integers
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0]+numbers[1]
# Complementary DNA
def DNA_strand(dna):
    res = ""

    for base in dna:
        if base == "A": res+="T"
        elif base == "T": res+="A"
        elif base == "C": res+="G"
        else: res+="C"

# Beginner Series #3 Sum of Numbers
def get_sum(a,b):
    return sum(range(min(a, b), max(a,b)+1))

# Friend or Foe?
def friend(x):
    res = []
    for i in x:
        if len(i) == 4:
            res.append(i)
    return res

# Credit Card Mask
def maskify(cc):
    if len(cc) <= 4:
        return cc
    res = ""
    for i in range(len(cc)):
        if i < len(cc) - 4:
            res+="#"
        else: res+=cc[i]
    return res

# საკლასო დავალება:

# შეასრულეთ ამოცანა:

# https://www.codewars.com/kata/551f37452ff852b7bd000139

def add_binary(a,b):
    return bin(a + b)[2:]

# 2-6)

# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132
def validate_pin(pin):
    return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()
# https://www.codewars.com/kata/56606694ec01347ce800001b
def is_triangle(a, b, c):
    return a+b>c and b+c>a and c+a>b
# https://www.codewars.com/kata/5656b6906de340bd1b0000ac
def longest(a1, a2):
    return "".join(sorted(set(a1+a2)))
# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa
def open_or_senior(data):
    res = []
    
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            res.append("Senior")
        else:
            res.append("Open")
    
    return res
# https://www.codewars.com/kata/56269eb78ad2e4ced1000013
def find_next_square(sq):
    
    # შევამოწმოთ თუ არის perfect square
    if int(sq**0.5)*int(sq**0.5) != sq: return -1

    # დავაბრუნოთ შემდეგი perfect square
    return (int(sq**0.5)+1)**2