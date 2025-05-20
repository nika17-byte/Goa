# The Wide-Mouthed frog!
def mouth_size(animal): 
    if animal.lower() == "alligator": return "small"
    return "wide"
# Get Nth Even Number
def nth_even(n):
    return n*2 - 2
# Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence
def replace_exclamation(st):
    res = ""
    
    for i in st:
        if i.lower() in "aeiou":
            res += "!"
        else:
            res += i
    
    return res
# 5 without numbers !!
def unusual_five():
    return len("asdfg")
# Add Length
def add_length(str_):
    res = []
    
    for i in str_.split(" "): res.append(f"{i} {len(i)}")
    
    return res

def add_length(str_):
    return [f"{i} {len(i)}" for i in str_.split(" ")]
# საკლასო დავალება:

# https://www.codewars.com/kata/54ff3102c1bad923760001f3