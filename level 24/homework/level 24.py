from turtle import *
# 2) ახსენით რა არის ფუნქცია და რატომ ჯობია მისი გამოყენება
# ფუნქცია არის კოდის წერის გამარტივებული სახე,რომელიც სხვადასხვა დავალებებს და მოქმედებებს ასრულებს
# 3) slicing და indexing დავალებები:
# Get the first element from a list.
# Get the last element from a list using negative indexing.
# Slice the first three elements of a list.
# Extract the last five elements from a string.
# Reverse a string using slicing.
# Get every third element from a list - ყოველი მესამე ელემენტი სიიდან
# Split a list into two halves using slicing. - ორ ნაწილად დაყავით სია (სიის სიგრძე აიღეთ ლუწი)
list = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8]
print(list[0])
print(list[-1])
print(list[0:3])
print(list[3:9])
print(list[-1:-8:-1])
print(list[2:9:3])
print(list[0:4])
print(list[4:9])
# 4) Boss level:
# ააგეთ 4 კვადრატი ისე, როგორც მე გავაკეთე, ანუ სამივე მიდგომით
def draw_square(x_coordinate, y_coordinate):
    penup()
    goto(x_coordinate, y_coordinate)
    pendown()

    for i in range(4):
        forward(200)
        left(90)

draw_square(100, 100)
draw_square(-300, 100)
draw_square(-300, -300)
draw_square(100, -300)

exitonclick()