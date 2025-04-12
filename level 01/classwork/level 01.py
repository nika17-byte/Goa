#name = "nika"
#name არის ცვლადი
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო
#"nika" არის ცვლადისთვის მნიშვნელობა

surname = "samkharadze"

#print(name)
#პრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი

name = "nika"    #ეს არის str (string)  ტიპის ცვლადი
age = 14       #ეს არის int(integer) მთელი რიცხვი
height =165.4  #ეს არის float ტიპის ცვლადი (ათწილადი)


knows_programming = True    #True ან False,  boolean (bool) ტიპის ცვლადი
is_ugly = False   #snakecase(უბრალოდ წერის სტილი სტანდარტულად)

isUgly = False  #ჯავასკრიპტული camelcase


# print(name + age)

#სტრინგი არის ბრჭყალებში მოქცეული სიმბოლოები
#print(name +" "+surname)

print(type(age))
print(type(name))
print(type(surname))
print(type(height))
print(type(knows_programming))

print(name + " "+str(age))
print("me mqvia" +" "+name + "," + "var" +" "+str(age) +" "+"wlis" + ","  + "chemi gvaria" +" "+surname + "," + "simageshi var" +" "+str(height) +" " +"cm")