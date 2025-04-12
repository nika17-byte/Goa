# საკლასო დავალება:

# შექმენით ფუნქცია სახელად manual_list, რომელსაც ექნება 4 პარამეტრი: start, end, step, user_num.

# თქვენი დავალებაა, რომ ფუნქციამ დააბრუნოს სია, რომელშიც იქნება რიცხვები არჩეული (start, end, step) დიაპაზონის მიხედვით, უბრალოდ ეს რიცხვები მეტი უნდა იყოს user_num.

# ფუნქცია გამოიძახეთ 3-ჯერ, განსხვავებული არგუმენტებით
def manual_list(start,end,step,user_num):
    result =  [i for i in range(start,end,step) if i > user_num]
    return result
print(manual_list(2, 5, 3, 5))
print(manual_list(10, 30, 6, 25))
print(manual_list(0, 40, 5, 10))

# Create a list comprehension that generates a list of all numbers between 1 and 100 that are divisible by either 3 or 5, but not both.
list1 = [n for n in range(1 , 101) if n % 3 == 0 or n % 5 == 0]
print(list1)
# Create a list comprehension that generates a list of all palindromic numbers between 10 and 200 (a palindromic number reads the same forward and backward).
list2 = [x for x in range(10 , 201) if str(x) == str(x)[::-1]]
print(list2)