# ```საკლასო დავალება 1: 0-დან 20-მდე დაბეჭდეთ ლუწი რიცხვები. არ გამოიყენოთ if - პირობითი განცხადება.```
for i in range(0 , 20 , 2):
    print(i)
# ```საკლასო დავალება 2: 0-დან 20-მდე დაბეჭდეთ კენტი რიცხვები. არ გამოიყენოთ if - პირობითი განცხადება.```
for i in range(1 , 20 , 2):
    print(i)
# ```საკლასო დავალება 3: 10-დან 30-ის ჩათვლით დაბეჭდეთ ყველა რიცხვი და თან მიუწერეთ ლუწია თუ კენტი, მაგ: 10 - even, 11 - odd, 12 - even და ასე გაგრძელდება 30-ის ჩათვლით```
for i in range(10, 30):
    if i % 2 == 0:
        print(i , "- even")
    else:
        print(i , "- odd")
#```საკლასო დავალება: მომხმარებელს შემოატანინეთ 2 რიცხვი, num1, num2.
#თუ პირველი მეტია მეორეზე, შექმენით დიაპაზონი მეორე რიცხვიან პირველი რიცხვის ჩათვლით და დაბეჭდეთ მხოლოდ ლუწი.
#ხოლო თუ მეორე რიცხვი მეტია პირველზე, შექმენით დიაპაზონი პირველიდან მეორეს ჩათვლით და დაბეჭდეთ მხოლოდ კენტი რიცხვები.
#საბოლოოდ დაბეჭდეთ ყველა ამ დაბეჭდილი რიცხვის ჯამი.```
num1=int(input("Enter your number:"))
num2=int(input("Enter your number:"))
if num1>num2:
    for i in range(num2,num1):
        if i%2==0:
            print(i)
            sum=sum+i
else:
    for i in range(num1,num2):
        if i%2==1:
            print(i)
            sum = sum+i
print(sum)