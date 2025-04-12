# while ციკლს ვიყენებთ მაშინ,როდესაც არ გვაქვს მოცემული იტერაციების რიცხვი
# ხოლო for ციკლს ვიყენებთ მაშინ,როდესაც გვაქვს მოცემული იტერაციების რიცხვი
# 4) დაბეჭდეთ "GOA BEST!!!" 50-ჯერ, ორივე ციკლით შეასრულეთ ეს დავალება
for i in range(50):
    print("GOA BEST!!!")
count = 0
while count < 50:
    print("GOA BEST!!!")
    count += 1
# 5) Write a program that uses a while loop to count from 1 to 10 and prints each number.\
count1  = 0
while count1 < 10:
    print(count1)
    count1 += 1
# 6) Use a while loop to print all even numbers between 1 and 20.
num1 = 2
while num1 < 20:
    print(num1)
    num1 += 2
# 7) Create a countdown from 10 to 1 using a while loop, and print "Blast off!" when the countdown finishes.
num2 = 10
while num2 > 0:
    print(num2)
    num2 -= 1
print("Blast off!")
# 8) Prompt the user to enter a password. Keep asking until they enter the correct password.
correct_password = "nika123"  
attempts = 0
user_password = ""  
while user_password != correct_password:
    attempts += 1
    user_password = input("enter password: ")
print("Access granted!")
# 9) Create a program that keeps asking for a username and password until both are correct.
correct_username = "nika"
attempts1 = 0
user_username = ""
while user_username != correct_username:
    attempts1 += 1
    user_username = input("Enter username: ")
correct_password1 = "nika17"
attempts2 = 0
user_password1 = ""
while user_password1 != correct_password1:
    attempts2 += 1
    user_password1 = input("Enter password: ")
print("Acces granted!")
# 10) Boss level: Use a while loop to calculate the factorial of a given number.
num3 = int(input("Enter number: "))
factorial = 1
while num3 > 0:
    factorial *= num3
    num3 -= 1
print("The factorial of your number is",str(factorial))