from turtle import *
# საკლასო დავალება:
# შექმენით ფუნქცია რომელიც მიიღებს ორ პარამეტრს - main_list, indexes_list.
# თქვენი დავალებაა, რომ indexes_list სიაში რა ინდექსებიც იქნება მოცემული, მთავარ სიაში, მაგ ინდექსებზე წაშალოთ ელემენტები
def remove_by_indexes(main_list, indexes_list):
    for index in sorted(indexes_list, reverse=True):
        if 0 <= index < len(main_list):
            main_list.pop(index)
    return main_list

main_list = [10, 20, 30, 40, 50]
indexes_list = [1, 3]

result = remove_by_indexes(main_list, indexes_list)
print(result)
# შექმენით ფუნქცია სახელად remove_one_element, რომელსაც გადაეცემა სია და ინდექსი.
# სიიდან მაგ ინდექსზე მყოფი ელემენტი ამოშალეთ და დაბეჭდეთ სია.
def remove_one_element(list, index):
    if 0 <= index < len(list):
        list.pop(index)
    else:
        print("wrong index!")
    print(list)
my_list = [10, 20, 30, 40, 50]
remove_one_element(my_list, 2)


