from turtle import *
# საკლასო დავალება:
# შექმენით ფუნქცია სახელად generate_big_sentence, რომელსაც გადაეცემა 3 პარამეტრი - name, surname, age.
# ფუნქციამ უნდა გამოგვიტანოს წინადადება ზუსტად იგივე წყობით, როგორც მე დავწერე (გადახედეთ რესურებს), გამოიყენეთ format ფუნქცია.
# სანამ ფუნქციას გამოიძახებთ, მომხმარებელს შემოატანინეთ ტერმინალიდან სახელი, გვარი, ასაკი და შეინახეთ ისინი ცვლადებში.
# ფუნქციის გამოძახებისას, მას არგუმენტებად უნდა გადაეცეს ეს ცვლადები
def generate_big_sentence(name , surname , age):
    print("My name is {} ,my surname is {} and I am {} years old.".format(name, surname, age))
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")
generate_big_sentence(name, surname, age)
# საკლასო დავალება:
# თქვენს ფუნქციაში format ფუნქციის მაგივრად გამოიყენეთ f string
def generate_big_sentence(name , surname , age):
    print(f"My name is {name} ,my surname is {surname} and I am {age} years old.")
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")
generate_big_sentence(name, surname, age)
# საკლასო დავალება:
# შექმენით ფუნქცია სახელად my_split, რომელსაც გადაეცემა ორი პარამეტრი - main_string და string_to_split.
# ფუნქციამ უნდა დაბეჭდოს სია - main_string გაიხლიჩოს string_to_split-ის მიხედვით.
# ფუნქციის გამოძახებამდე მომხარებელს შემოატანინეთ მთავარი და დასაყოფი სთრინგები, 
# შეინახეთ ცვლადებში. შემდეგ გამოიძახეთ ფუნქცია და ეს ცვლადები გადაეცით არგუმენტებად
def my_split(main_string, string_to_split):
    split_list = main_string.split(string_to_split)
    print(split_list)

main_string = input("Enter the main string: ")
string_to_split = input("Enter the string to split by: ")

my_split(main_string, string_to_split)
# საკლასო დავალება:შექმენით ფუნქცია სახელად manual_append. 
# ამ ფუნქციამ სიის ბოლოში უნდა ჩაამატოს ახალი ელემენტი.არ გამოიყენოთ append, 
# გამოიყენეთ insert.ფუნქციას ექნება 2 პარამეტრი - main_list, item_to_insert.
def manual_append(main_list, item_to_insert):
    main_list.insert(len(main_list), item_to_insert)
main_list = [1, 5, 7]
item_to_insert = 4

manual_append(main_list, item_to_insert)
print(main_list)
