# ციკლი არის პროგრამირების კონსტრუქცია, რომელიც საშუალებას გვაძლევს შევასრულოთ ერთი და იგივე კოდი რამდენჯერმე. 
# იგი გამოიყენება, როდესაც ერთი და იგივე ოპერაცია რამდენჯერმე უნდა განმეორდეს - მაგალითად, მონაცემთა მასივის 
# დამუშავება ან ოპერაციების განსაზღვრული რაოდენობის შესრულება. ციკლებს აქვთ განსხვავებული სტრუქტურა სხვა 
# პროგრამირების ენებში, მაგალითად, სხვა პროგრამირების ენებში: for loop, while loop და do-while ციკლი. 
# გამეორება არის თითოეული ციკლის შესრულების განმეორება. მაგალითად, როდესაც ჩვენ ვასრულებთ for loop-ს 10-ჯერ, 
# თითოეული ციკლის შესრულება განიხილება იტერაციად.

x = range(20 , 50)

y = range(100 , 150)

z = range(20 , 50 , 2)

a = range(11 , 31 , 2)

for i in range(10):
    print("Nika Samkharadze")

for i in range(10 , 31):
    print(i / 2)

for i in range(40 , 60):
    print(i ** 3)

for i in range(5):
    num = int(input("Enter number: "))
    print(num)

name = input("Enter your name: ")
for i in name:
    print(i)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
a = range(num1 , num2 , num3)
for i in a:
    print(i ** 2)

sum = 0
for i in range(5 , 16):
    sum += i
print(sum)