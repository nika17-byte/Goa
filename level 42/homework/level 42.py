# 2) თქვენი სიტყვებით ახსენით dictionary რითი განსხვავდება აქამდე ნასწავლი კოლექციებისგან, რა არის key, value, key-value pair
# dictionary შედგება key-სა და value-სგან,ასევე მასში შემავალი ელემენტების შეცვლა შეგვიძლია,ანუ არის muttable.key არის იდენტიფიკატორი,რომელშიც ინახება value
# key-value pair არის მონაცემთა შენახვის სტრუქტურა ,რომელსაც აქვს გასაღები და შესაბამისი მნიშვნელობა
# 3) Create a dictionary with at least five key-value pairs and print all the keys using the keys() method.
dict1 = {
    "name" : "Nika",
    "surname" : "Samkharadze",
    "academy" : "GOA",
    "fav-color" : "red",
    "city" : "Rustavi"
}
print(dict1.keys())
# 4) Create a dictionary and print all the values using the values() method.
dict2 = {
    "name" : "Nika",
    "surname" : "Samkharadze",
    "academy" : "GOA",
    "fav-color" : "red",
    "city" : "Rustavi"
}
print(dict2.values())
# 5) Create a dictionary and print all key-value pairs using the items() method.
dict3 = {
    "name" : "Nika",
    "surname" : "Samkharadze",
    "academy" : "GOA",
    "fav-color" : "red",
    "city" : "Rustavi"
}
print(dict3.items())
# 6) Iterate over a dictionary using the items() method and print each key with its corresponding value.
dict4 = {
    "name" : "Nika",
    "surname" : "Samkharadze",
    "academy" : "GOA",
    "fav-color" : "red",
    "city" : "Rustavi"
}
print(dict4.items())
# 7) Create a dictionary and check if a specific key exists using the in operator.
dict5 = {
    "name" : "Nika",
    "surname" : "Samkharadze",
    "academy" : "GOA",
    "fav-color" : "red",
    "city" : "Rustavi"
}
key_to_check = "academy"
if key_to_check in dict5:
    print(key_to_check)
# 8) Retrieve a value from a dictionary using the get() method and handle cases where the key does not exist.
dict6 = {
    "name" : "Nika",
    "surname" : "Samkharadze",
    "academy" : "GOA",
    "fav-color" : "red",
    "city" : "Rustavi"
}
name = dict6.get("name")
print(f"Name: {name}")
country = dict6.get("country")
print(f"Country: {country}")
# 9) Add a new key-value pair to an existing dictionary and print the updated dictionary.
dict7 = {
    "name" : "Nika",
    "surname" : "Samkharadze",
    "academy" : "GOA",
    "fav-color" : "red",
    "city" : "Rustavi"
}
dict7["country"] = "Georgia"
print(dict7)
# 10) Remove a key-value pair from a dictionary using the pop() method and print the updated dictionary.
dict8 = {
    "name" : "Nika",
    "surname" : "Samkharadze",
    "academy" : "GOA",
    "fav-color" : "red",
    "city" : "Rustavi"
}
dict8.pop("academy")
print(dict8)
# 11) Update an existing dictionary with another dictionary using the update() method.
my_info = {
    "name" : "nika",
    "age" : "14",
}

updated_info = {
    "age" : "15",
    "country" : "georgia"
}
my_info.update(updated_info)
print(my_info)
# 12) Create a dictionary and print its length using the len() function.
dict9 = {
    "name" : "Nika",
    "surname" : "Samkharadze",
    "academy" : "GOA",
    "fav-color" : "red",
    "city" : "Rustavi"
}
print(len(dict9))
# 13) Write a function that returns the sum of all numeric values in a dictionary.
sum = {    
    "num1" : 5,
    "num2" : 6,
    "num3" : 7
}
print(sum["num1"] + sum["num2"] + sum["num3"])
# 14) Clear all elements from a dictionary using the clear() method and print the result.
sum = {    
    "num1" : 5,
    "num2" : 6,
    "num3" : 7
}
sum.clear()
print(sum)
# 15) Create dictionary about your information, use at least 10 key-value pairs
dict10 = {
    "name" : "Nika",
    "surname" : "Samkharadze",
    "academy" : "GOA",
    "fav-color" : "red",
    "city" : "Rustavi",
    "country" : "georgia",
    "sport" : "basketball",
    "weight" : 60,
    "height" : 170,
    "gender" : "male"
}