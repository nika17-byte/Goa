# საკლასო დავალება: მომხმარებელს შემოატანინეთ რიცხვი და შეინახეთ ის ცვლადში მთელი რიცხვის სახით.

# შემდეგ შექმენით დიაპაზონი 0-დან ამ რიცხვამდე და დაბეჭდეთ დიაპაზონის ყველა რიცხვის ჯამი.

# გამოიყენეთ for ციკლი


num = int(input("Enter number: "))
total_sum = 0
for i in range(num + 1):  
    total_sum += i
print(total_sum)


correct_password = "nika123"  
attempts = 0
user_password = ""  
while user_password != correct_password:
    attempts += 1
    user_password = input("enter password: ")
    print("Wrong password,try again!")
print("Access granted!")

my_num = 6
attempts = 0
user_guess = None
while user_guess != my_num:
    attempts += 1
    user_guess = int(input("guess number between 1 to 10: "))
    while user_guess > my_num:
        print("less.")
        user_guess = int(input("try again: "))
        attempts += 1
    while user_guess < my_num:
        print("higher.")
        user_guess = int(input("try again: "))
        attempts += 1
print("you guessed it!.")