# 2) თქვენი სიტყვებით ახსენით რა განსხვავებაა format ფუნქციასა და f სთრინგს შორის, ასევე რა განსხვავებაა 
# append-სა და insert-ს შორის 
# format ფუნქციასა და f სთრინგს შორის ისაა განსხვავება,
# რომ format ფუნქცია იწერება სთრინგის ბოლოს,ხოლო f სთრინგის გამოყენებისას f იწერება სთრინგის წინ და
#  სთრინგში მოცემულ კნაკლილ ხაზებში ვწერთ ცვლადების სახელებს.append-სა და insert-ს შორის კი ისაა განსხვავება,
# რომ append ფუნქციას სთრინგი ცხრილის ბოლოს გამოაქვს,ხოლო insert ფუნქციას კონკრეტული სთრინგი გამოაქვს კონკრეტულ ინდექსზე
# 3) Write a function that takes a user's name and age, and returns a welcome message formatted with an f-string.
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
print(f"Welcome {name}")
# 4) Write a function that takes a first name and last name, capitalizes them, and formats them into a single string.
firstname = str(input("Enter your firstname: "))
lastname = str(input("Enter your lastname: "))
print(f"Hello {firstname.capitalize()} {lastname.capitalize()}")
# 5) Create a function that takes a string, reverses it, and formats it within a sentence.
string= str(input("Enter string: "))
print(f"Your reversed string: {string[::-1]}")
# 6) Write a function that takes a sentence, a word, and an index, and inserts the word into the sentence at the given index.
def insert_word(sentence, word, index):
    if index < 0:
        index = 0
    elif index > len(sentence):
        index = len(sentence)
    print(sentence[:index] + word + sentence[index:])

sentence = input("Enter sentence: ")
word = input("Enter word: ")
index = int(input("Enter index: "))
insert_word(sentence, word, index)
# 7) Write a function that takes a sentence and returns a list of words.
def sentence_in_words(sentence):
    return sentence.split()
sentence = input("Enter sentence: ")
words = sentence_in_words(sentence)
print(f"List of words: {words}")
#8) Create a function that takes a string of comma-separated values (CSV) and returns a list of individual items.
def list(string):
    # სტრიქონი იყოფა მძიმის (',') გამოყენებით და გარდაიქმნება სიად
    return string.split(',')
#9) Write a function that takes a paragraph and splits it into sentences based on periods.
def my_split(main_string, string_to_split):
    split_list = main_string.split(string_to_split)
    print(split_list)

main_string = input("Enter the main string: ")
string_to_split = input("Enter the string to split by: ")

my_split(main_string, string_to_split)
#10) Write a function that takes a list and an item, and appends the item to the list.
def manual_append(main_list, item_to_append):
    main_list.append( item_to_append)
main_list = [1, 5, 7]
item_to_append = 4

manual_append(main_list, item_to_append)
print(main_list)
# 11) Create a function that takes a list and a list of items, and appends each item to the original list.
def append_items(original_list, items):
    original_list += items
    return original_list
# 12) Create a function that appends all elements of one list to another list.
def list(list1, list2):
    list1 += list2
    return list1
# 13) Write a function that takes a list, an index, and an item, and inserts the item at the specified index.
# ?
# 14) Create a function that inserts an item at the beginning of a list.
def insert_beggining(my_list,item):
    my_list.insert(0 , item)
my_list = ["goa" , "ball" , "nika"]
item = "chama"
insert_beggining(my_list,item)
print(insert_beggining)
# 15) Create a function that inserts an item at the end of a list using the insert method.
def insert_last(list,items):
    list.insert(4 , items)
list = ["goa" , "nika" , "samkharadze" , 14 , "programming"]
items = "chama"
insert_last(list , items)
print(insert_last)