def get_average(marks):
    return sum(marks) // len(marks)

def hoop_count(n):
    if n < 10: return "Keep at it until you get it"
    return "Great, now move on to tricks"

def reverse_words(s):
    return " ".join(s.split(' ')[::-1])

def cockroach_speed(s):
    return int(s*27.777778)

def switch_it_up(number):
    res = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    return res[number]

def square(n):
    return n*n

def remove_every_other(my_list):
    new_list = []
    
    for i in range(len(my_list)):
        if i%2 == 0: new_list.append(my_list[i])
    
    return new_list

def twice_as_old(dad_years_old, son_years_old):
    res = (dad_years_old - 2 * son_years_old)
    
    if res < 0: return res*-1
    return res

def str_count(strng, letter):
    return strng.count(letter)

def is_even(n): 
    return n % 2 == 0

def move(position, roll):
    return position + roll*2

def powers_of_two(n):
    return [2**y for y in range(n + 1)]

def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
    return None

def to_alternating_case(string):
    return string.swapcase()

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

def bonus_time(salary, bonus):
    if bonus:
        return f"${salary * 10}"
    else:
        return f"${salary}"
    
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0
    
def sum_str(a, b):
    return str(int(a or '0') + int(b or '0'))