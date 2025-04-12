# 2) თქვენი სიტყვებით ახსენით რა არის elif და რაში ვიყენებთ მას
# elif არის ბრძანება რომელიც გამოიყენება if ბრძანების შემდეგ და მის დასაწერად აუცილებელია პირობის გაწერა
# 3) Write a program that takes three numbers as input and prints the largest of the three.
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
num3 = int(input("Enter number: "))
if num1 > num2 and num1 > num3:
    print(num1, "-largest number")
elif num2 >= num1 and num2 >= num3:
    print(num2, "-largest number")
else:
    print(num3, "-largest number")
# 4) Write a program that takes a score (0-100) as input and outputs the grade based on the following rules:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F
num4 = int(input("Enter score: "))
if 90 <= num4 <= 100:
    print("grade = A")
elif 80 <= num4 <= 89:
    print("grade = B")
elif 70 <= num4 <= 79:
    print("grade = C")
elif 60 <= num4 <= 69:
    print("grade = D")
elif 0 <= num4 < 60:
    print("grade = F")
else:
    print("Enter a number between 0 and 100!!!!!!!!!!!!!!!!!!!!!!!!!")
# 5) Write a program that takes a number as input and prints whether it is positive, negative, or zero.
num5 = int(input("Enter number: "))
if num5 > 0:
    print(num5, "-positive number")
elif num5 < 0:
    print(num5, "-negative number")
elif num5 == 0:
    print(num5, "-zero")
# 6) Use a loop to calculate the sum of numbers between two given integers.
num6 = int(input("Enter number: "))
num7 = int(input("Enter number: "))
sum = num6 + num7
for i in range(num6, num7 +1):
    sum += i
print("the sum of", num6, "and", num7,"is", sum)
# 7) Write a program that checks if a single given number is prime number
num8 = int(input("Enter number: "))
# ?
# 8) Create a list of five numbers and print the first, third, and last elements using indexing.
list = [1 , 2 , 3 , 4 , 5]
number1 = list[0]
number2 = list[2]
number3 = list[4]
print(number1,number2,number3)
# 9) Create a list of 20 elements (any data type) and print all of the elements - use indexing
list1 = [1 , "goa" , "ball" , "banana" , 3.14 , 40 , "pc" , "nika" , 40.09 , 95 , 10 , 98 , "egg" , "wall" , 39.1 , 19 , "pen" , "book" , 980.12 , "ten"]
print(list1[0] , list1[1] , list1[2],list1[3],list1[4],list1[5],list1[6],list1[7],list1[8],list1[9],
list1[10],list1[11],list1[12],list1[13],list1[14],list1[15],list1[16],list1[17],list1[18],list1[19],)