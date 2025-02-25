# საკლასო დავალება
# შექმენით dictionary, სადაც იქნება შემდეგი გასაღებები: name, surname, academy, fav-color, city, goa-student, age, fav-programming-lang.
# შემდეგ დაბეჭდეთ ამ dict-ის თითოეული მნიშვნელობა
dict1 = {
    "name" : "Nika",
    "surname" : "Samkharadze",
    "academy" : "GOA",
    "fav-color" : "red",
    "city" : "Rustavi",
    "goa-student" : "True",
    "age" : "14",
    "fav-programming-lang" : "Python"
}
print(dict1["name"])
print(dict1["surname"])
print(dict1["academy"])
print(dict1["fav-color"])
print(dict1["city"])
print(dict1["goa-student"])
print(dict1["age"])
print(dict1["fav-programming-lang"])
# Create a Python program that initializes a dictionary with at least five key-value pairs. Perform the following operations:

# Print all the keys in the dictionary using the keys() method.
# Print all the values in the dictionary using the values() method.
# Print all key-value pairs using the items() method.
# Iterate over the dictionary using the items() method and print each key with its corresponding value in a formatted string.
dict2  = {
    "name" : "Nika",
    "surname" : "Samkharadze",
    "academy" : "GOA",
    "fav-color" : "red",
    "city" : "Rustavi"
}
print(dict2.keys())
print(dict2.values())
print(dict2.items())
for key, value in dict2.items():
    print(f"{key}: {value}")