# საკლასო დავალება:
# მომხმარებელს შემოატანინეთ სახელი და შეინახეთ name ცვლადში.
# შემდეგ შემოატანინეთ არჩევანი (რომელიც იქნება "u" ან "l") და შეინახეთ ეს ინფორმაცია choice ცვლადში.
# თუ choice ტოლია "u"-სი, მაშინ მომხმარებლის სახელი გამოიტანეთ uppercase-ში.
# თუ choice ტოლია "l"-ის, მაშინ მომხმარებლის სახელი გამოიტანეთ lowercase-ში.
# სხვა შემთხვევაში, დაუბეჭდეთ wrong information.
name = str(input("Enter your name: "))
choice = str(input("Choose one of them:u or l: "))
if choice == "u":
    print(name.upper())
elif choice == "l":
    print(name.lower())
else:
    print("wrong information")

# შექმენით ფუნქცია, სახელად manual_find, რომელსაც გაწერილი ექნება 2 პარამეტრი: main_string და str_to_find.
# ამ ფუნქციის დავალებაა რომ main_string-ში იპოვოს str_to_find მერამდენე ინდექსზეა.
# თუ მთავარ სთრინგში საძიებელი სთრინგი უბრალოდ არ გვაქვს, დავბეჭდოთ -1
def manual_find(main_string , str_to_find):
    for i in range(len(main_string) - len(str_to_find) + 1):
        if main_string[i:i+len(str_to_find)] == str_to_find:
            return i
    return -1
print(manual_find("hi", "ball")) 
print(manual_find("bye", "home"))
# საკლასო დავალება:
# მომხმარებელს შემოატანინეთ მთავარი სთრინგი და შეინახეთ main_str ცვლადში.
# შემდეგ შემოატანინეთ დასათვლელი სთრინგი და შეინახეთ str_to_cout nცვლადში.
# დაბეჭდეთ str_to_count რამდენჯერ შეგხვდება main_str ცვლადში
main_str = str(input("Enter main string: "))
str_to_count = str(input("Enter string to count: "))
print(main_str.count(str_to_count))
# საკლასო დავალება:
# შექმენით ფუნქცია სახელად manual_swapcase
def manual_swapcase(n):
    new_string = ""
    for char in n:
        if char.isupper():
            new_string += char.lower()
        elif char.islower():
            new_string += char.upper()
        else:
            new_string += char
    return new_string
print(manual_swapcase("bananas")) 
print(manual_swapcase("mangos"))