car = {}
n=int(input("Enter the number of inputs:-"))
for i in range(n):
    brand = input("Enter car brand : ")
    color = input("Enter car color : ")

    car[brand] = color



print(car)
f = open('python.txt', 'w')
print(car, file = f)
1