# საკლასო დავალება: შექმენით სია, რომელშიც იქნება 10 ელემენტი. 
# შემდეგ მომხმარებელს შემოატანინეთ რიცხვი და შეინახეთ მთელი რიცხვის სახით.
# თუ ეს რიცხვი მეტია ან ტოლია 0-ზე და ნაკლებია სიის სიგრძეზე, მაშინ სიიდან ამ ინდექსზე მყოფი ელემენტი წამოიღეთ და დაბეჭდეთ.
# თუ ეს რიცხვი მეტია ან ტოლია "სიის სიგრძე გამრავლებული -1ზე" და ნაკლებია ან ტოლია -1 ზე, მაშინ დაბეჭდეთ ამ ინდექსზე მყოფი ელემენტი
list = [1 , "apple" , 3.14 , "goa" , 30 , 12 , 13.67 , "ball" , 9.4 , 19]
num1 = int(input("Enter number: "))
if num1 >= 0 and num1 < 10:
    if num1 >=  0 and num1 < 10:
        print(list[num1-1])
elif num1 >= -10 and num1 <= -1:
    print(list[num1+1])
else:
    print("Wrong index")


# საკლასო დავალება: მოცემულია სია list1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]. გადაუარეთ სიას და დაბეჭდეთ მისი ელემენტი გამრავლებული 2-ზე, ასევე გაყოფილი 2-ზე
list1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
for x in list1:
    print(x * 2)
    print(x / 2)