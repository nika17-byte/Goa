from turtle import *
# საკლასო დავალება:

# შექმენით tuple სადაც შეინახება 10 ელემენტი.

# დაბეჭდეთ თითოუელი ელემენტი, ინდექსების გამოყენებით
tuple1 = (1,2,3,4,5,6,7,8,9,10)
for i in tuple1:
    print(i)

# საკლასო დავალება:

# შექმენით ფუნქცია სახელად no_duplicates, რომელსაც გადაეცემა ერთი პარამეტრი - user_list.

# user_list-ის მონაცემთა ტიპია სია, ხოლო თქვენი დავალებაა რომ ფუნქციამ დააბრუნოს ეს სია იმ სახით, რომ მასში დუპლიკატები არ გვქონდეს. 

# ფუნქცია გამოიძახეთ 3-ჯერ, განსხვავებული არგუმენტებით
def no_duplicates(user_list):
    return list(set(user_list))

list1 = [1, 2, 3, 1, 2, 4]
list2 = ["a", "b", "a", "c", "d", "b"]
list3 = [16, 10, 16, 20, 10, 20]

print(no_duplicates(list1))
print(no_duplicates(list2))
print(no_duplicates(list3))