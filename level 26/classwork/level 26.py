# შექმენით ფუნქცია სახელად greet, რომელსაც ექნება 1 პარამეტრი. ფუნქციის გამოძახებისას არგუმენტად გადაეცით თქვენი სახელი და ფუნქციამ ასეთი რამ უნდა დაგიბეჭდოთ: "გამარჯობა, {აქ თქვენი სახელი}"
def greet(name):
    print("გამარჯობა,",name)
greet("nika")
# საკლასო დავალება: შექმენით ფუნქცია სახელად manual_range, რომელსაც გადაეცემა სამი პარამეტრი (start, end, step).
# ფუნქციის დავალებაა რომ გადაცემული პარამეტრებით შეადგინოს დიაპაზონი, შემდეგ ამ დიაპაზონს გადავუაროთ ციკლით და დავბეჭდოთ მხოლოდ ლუწი რიცხვები.
#ფუნქციის გამოძახებისას მას აუცილებლად უნდა გადაეცეს 3 არგუმენტი.
#ფუნქცია გამოიძახეთ მინიმუმ 5-ჯერ სხვადასხვა არგუმენტებით
def manual_range(start,end,step):
    for i in range(start,end,step):
        if i % 2 == 0:
            print(i)
        else:
            print("other nums are odd")
manual_range(2, 4, 1)
manual_range(3, 10, 2)
manual_range(2, 6, 2)
manual_range(1, 80, 2)
manual_range(9, 70, 5)
# საკლასო დავალება: შექმენით ფუნქცია სახელად manual_len, რომელსაც ექნება გაწერილი 1 პარამეტრი.
#ფუნქციას გადაეცემა სია და მისი დავალებაა რომ დააბრუნოს სიის სიგრძე (len არ გამოიყენოთ). უნდა გამოიყენოთ for ან while ციკლი და ერთი ცვლადი. საბოლოოდ დაბეჭდეთ სიის სიგრძე.
#ფუნქციის გამოძახებისას გადაეცემა მას ერთი არგუმენტი - სია
def manual_len(age):
        length = 0
        for i in age:
            length += 1
list1 = [1, 2, 3, 4, 5]
print("სიის სიგრძე:", manual_len(list1))