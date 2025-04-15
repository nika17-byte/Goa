# 2. **User Input Number Division**  
#    Ask the user to enter two numbers and divide them. Handle errors like division by zero and non-numeric input.
# try:
#     num1 = float(input("Enter number: "))
#     num2 = float(input("Enter number: "))
#     print("Result:", num1 / num2)
# except ValueError:
#     print("Enter numeric number")
# except ZeroDivisionError:
#     print("Enter non-zero number")
# 3. **List Index Access**  
#    Create a small list and ask the user for an index to access. Handle the case when the index is out of range.
# try:
#     list1 = [1 , 2 , 3 ,  4 , 5 , 6 , 7 , 8]
#     Index1 = int(input("Enter index: "))
#     print("the number on your index is:",list1[Index1])
# except IndexError:
#     print("Index is out of range,enter index from 0 to 7")
# 4. **Dictionary Key Access**  
#    Use a dictionary and try to access a key that might not exist. Handle the possible error.
#     dict = {
#         "name" : "nika",
#         "surname" : "samkharadze"
#     }
# try:
#     print("age:",dict[age] )
# except KeyError:
#     print("Wrong key,use name or surname key")
# 5. **Convert String to Integer**  
#    Ask the user for a number and convert it to an integer. Handle the error if they enter something that can't be converted.
try:
    num3 = int(input("Enter number: "))
    print(f"Your number is {num3}.")
except ValueError:
    print("Enter valid number!")

# 6. **Function as Argument – Greeting**
# Write a function that takes another function as an argument and calls it to print a greeting.
def greeting():
    print("Welcome!")

def another_function(hello):
    hello()

another_function(greeting)
# 7. **Return a Function – Multiplier**
# Create a function that returns another function which multiplies any number by a given factor.
def Multiplier(factor):
    def multiply_by(i):
        return i * factor
    return multiply_by

double = Multiplier(2)
print(double(5)) 