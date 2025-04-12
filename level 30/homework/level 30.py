#2) Convert a given sentence to uppercase and print the result.
string = "sigma boy"
print(string.upper())
#3) Take a user's name input and display it in uppercase letters.
string1 = str(input("Enter your name: "))
print(string1.upper())
#4) Create a function that converts a list of lowercase strings to uppercase.
list = ["ball" , "sigma" , "mma" , "goa"]
for i in list:
    print(i.upper())
#5) Convert all the characters of a given sentence to lowercase and print it.
string2 = "HELLO wOrLd"
print(string2.lower())
#6) Ask the user for their email address and ensure it is stored in lowercase.
string3 = str(input("Enter your email adress: "))
print(string3.lower())
# 7) Write a function that takes a mixed-case string and returns it in all lowercase letters.
string4 = "HeLlO GiNgEr"
print(string4.lower())
# 8) Capitalize the first letter of a sentence provided by the user.
string5 = str(input("Enter your name: "))
print(string5.capitalize())
# 9) Given a list of lowercase strings, capitalize the first letter of each string.
list1 = ["ball" , "nika" , "basketball" , "goa"]
for i in list:
    print(i.capitalize())
# 10) Create a function that takes a string and returns it with the first letter capitalized.
string6 = str(input("Enter string: "))
print(string6.capitalize())
# 11) Find the position of the first occurrence of the word "Python" in a sentence.
sentence = "goa - python html fun"
print(sentence.find("python"))
# 12) Search for a user-specified substring in a provided string and print its starting index.
string7 = input("Enter the main string: ")
substring = input("Enter the substring to search: ")
index = string7.find(substring)
if index != -1:
    print("The substring '" + substring + "' is found at index " + str(index))
else:
    print("The substring '" + substring + "' is not found in the main string")
# 13) Write a function to find and return the index of a specified character in a given string.
def find_char_index(string, char):
    return string.find(char)
string8 = str(input("Enter string: "))
char = str(input("Enter character: "))
result = find_char_index(string8, char)
if result != -1:
    print("The character '" + char + "' is found at index " + str(result))
else:
    print("The character '" + char + "' is not found in the string.")
# 14) Find and print the length of a user-provided string.
string9 = input("Enter string: ")
print(len(string9))
# 15) Write a function that takes a list of strings and returns their lengths.
list2 = ["nika" , "samxaradze" , "kahoot" , "goa" , "hotel"]
for i in list2:
    print(i.len())
# 16) Count the number of times the word "the" appears in a given paragraph.
p1 = "this is the most smallest phone in the world"
print(p1.count("the"))
#17) Ask the user to input a character and count its occurrences in a given string.
string10 = str(input("Enter string: "))
character = str(input("Enter character: "))
print(string10.count(character))
#18) Create a function that counts and returns the occurrences of a specified word in a text.
p2 = "the best sport in history is basketball.basketball is played with basketball ball,and in basketball there are many grat players"
print(p2.count("basketball"))
#19) Find and print the index of the first occurrence of the word "hello" in a given string.
p3 = "hello"
print(p3.index("h"))
#20) Write a function that returns the index of a character provided by the user in a string.
string11 = str(input("Enter string: "))
ch = str(input("Enter character: "))
print(string11.index(ch))
#21) Check if all characters in a given string are lowercase and print the result.
p4 = "helLo"
print(p4.islower())
#22) Create a function that takes a string and returns True if it is completely in lowercase, otherwise False.
string12 = str(input("Enter string: "))
print(string12.islower())
#23) Prompt the user to input a string and verify if it contains only lowercase letters.
string13 = str(input("Enter string: "))
print(string13.islower())
#24) Verify if all the characters in a user-provided string are uppercase.
string14 = str(input("Enter string: "))
print(string14.isupper())
#25) Write a function that checks if a string consists entirely of uppercase letters and returns a boolean result.
p5 = "HELLO"
print(p5.isupper())
#26) Check and display whether a string input by the user is in uppercase.
string15 = str(input("Enter string: "))
print(string15.isupper())
#27) Replace all occurrences of the word "dog" with "cat" in a given sentence.
p6 = "its hard to take care of dog"
print(p6.replace("dog" , "cat"))
#28) Write a function that replaces all spaces in a string with underscores.
p7 = "locked in for exam"
print(p7.replace(" " , "_"))
#29) Convert a string such that uppercase letters become lowercase and vice versa, then print the result.
p8 = "OEI OEI OEI URUNI MARANE QOQE OEI OEI OEI"
print(p8.swapcase())
#  30) Write a function that takes a sentence and returns it with swapped case for each letter.
sentence = str(input("Enter sentence: "))
print(sentence.swapcase())