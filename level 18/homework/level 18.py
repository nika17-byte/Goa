# 2) თქვენი სიტყვებით ახსენით როგორ მუშაობს პირობითი განცხადებები და გააკეთეთ ნახაზი
# არსებობს if,else და elif პირობითი განცხადებები,if პირობითი განცხადება გვჭირდება როდესაც რაიმე პირობის შემოწმება გვინდა
# else პირობით განცხადება გვჭირდება მაშინ თუ ერთი პირობაარ შესრულდება,მაშინ შეასრულოს სხვა პირობა
# 3) მომხმარებელს შემოატანინეთ 2 რიცხვი და დაბეჭდეთ მათ შორის უდიდესი
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
if num1 > num2:
    print(num1)
else:
    print(num2)
# 4) Write a program that checks if a given number is even or odd.
num3 = int(input("Enter number: "))
if num3 % 2 == 0:
    print(num3,"-even")
else:
    print(num3,"-odd")
# 5) Write a program to check if a number is positive or negative.
num4 = float(input("Enter number: "))
if num4 > 0:
    print(num4,"-positive")
else:
    print(num4,"-negative")
# 6) Write a program to check if a number is divisible by 5 - პროგრამა რომელიც ამოწმებს რიცხვი 5-ზე უნაშთოდ იყოფა თუ არა
num5 = int(input("Enter number: "))
if num5 % 5 == 0:
    print(num5,"-is diviseble by 5")
else:
    print(num5,"-isn't diviseble by 5")
# 7) Ask the user to enter a number multiple times and check if it's even or odd. Stop after 5 numbers.
for i in range(5):
    num6 = int(input("Enter number: "))
    if num6 % 2 == 0:
        print(num6,"-even")
    else:
        print(num6,"-odd")
# 8) Create a while loop that asks the user to enter a password. Keep asking until they enter the correct password "Goa best". Also print the count of incorrect passwords.
correct_password = "Goa best"
user_guess = input("Enter password: ")
counter = 0
while user_guess != correct_password:
    user_guess = input("Enter password: ")
    counter += 1
print("Access granted")
print("Your guess count:", str(counter))
# 9) Write a program that takes two numbers and an operator (+, -, *, /) as input and performs the calculation. Display the result and end the program.
num1 = float(input("Enter number: "))
num2 = float(input("Enter number: "))
operator = input("Choose one operator: +, -, *, /, **, %  ")

if operator == "+":
    print(num1, "+", num2, "=", num1+num2)
elif operator == "-":
    print(num1, "-", num2, "=", num1-num2)
elif operator == "*":
    print(num1, "*", num2, "=", num1*num2)
elif operator == "/":
    if num2 == 0:
        print("გაყოფა 0-ზე არ შეიძლება")
    else:
        print(num1, "/", num2, "=", num1/num2)
elif operator == "**":
    print(num1, "**", num2, "=", num1**num2)
elif operator == "%":
    print(num1, "%", num2, "=", num1%num2)
else:
    print("Wrong operator")