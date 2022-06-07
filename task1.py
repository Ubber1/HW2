a = int(input())
b = int(input())
c = int(input())

print("Введите число а", a)
print("Введите число b", b)
print("Введите число c", c)

if a+b>c:
    print ("Треугольник существует")
elif a+c>b:
    print ("Треугольник существует")
elif b+c>a:
    print ("Треугольник существует")
else:
    print("ошибка")

if a==b:
    print("равнобедренный")
elif a==b==c:
    print("равносторонний")
else:
    print("разносторонний")