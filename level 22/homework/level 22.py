# 2) თქვენი სიტყვებით ახსენით რა არის slicing, გააკეთეთ ნახაზი ამ საკითხზე
# slicing არის სიებში,taple-ებში კონკრეტული მონაკვეთის არჩევის მეთოდი
# 3) შექმენით სია, რომელშიც იქნება 10 ელემენტი. გადაუარეთ სიას ციკლით და დაბეჭდეთ მისი ყველა ელემენტი
list = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
for i in list:
    print(i)
# 4) შექმენით სია, რომელშიც იქნება 10 ელემენტი. მომხმარებელს შემოატანინეთ ორი მთელი რიცხვი, num1 და num2. 
# თუ num1 მეტია num2-ზე, slicing მოახდინეთ სიაზე num1 ინდექსიდან num2 ინდექსამდე და დაბეჭდეთ ახალი სია.
# თუ num2 მეტია num1-ზე, slicing მოახდინეთ სიაზე num2 ინდექსიდან num1 ინდექსამდე და დაბეჭდეთ ახალი სია.
# თუ ეს ორი რიცხვი ტოლია, დაბეჭდეთ ცარიელი სია.
list1 = ["goa" , "best" , "programming" , "academy" , 11 , 12 , 13 , 14 , 15 , 17]
num1 = int(input("Enter number from 0 to 9: "))
num2 = int(input("Enter number from 0 to 9: "))
if num1 > num2:
    result = list1[num2:num1]
    print("new list:", result)
elif num2 > num1:
    result = list1[num1:num2]
    print("new list:", result)
else:
    print("new list: []")
# 5) Given a list of numbers, print the first, third, and last elements using indexing.
list2 = [30 , 40 , 50 , 60 , 70 , 80]
print(list2[0] , list2[2] , list2[5])
# 6) Given a list of strings, print the list in reverse order using slicing.
list3 = ["house" , "court" , "arena" , "home" , "Goal Oriented Academy" , "basketball" , "iron"]
print(list3[-1:-8:-1])
# 7) Given a list of words, print every second element starting from the first element. (ერთი ელემენტის გამოტოვებით)
list4 = ["word" , "word1" , "word2" , "word3" , "word4" , "word5" , "word6" , "word7" , "word8" , "word9"]
print(list4[0:10:2])
# 8) Given a list of numbers, replace the fourth element with the number 100 and print the modified list.
list5 = [60 , 70 , 80 , 90 , 110 , 120]
list5[3] = 100
print(list5)