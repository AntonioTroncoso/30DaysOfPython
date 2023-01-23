
age = int(input('Enter age: '))
if age >= 18:
    print("You are old enough to drive.")
else:
    print("You need to wait", 18 - age, "years.")

my_age = 18

if age == my_age:
    print("Nosotros somos de la misma edad")
elif age > my_age:
    print("Tu eres", age - my_age, "años mayor que yo")
else:
    print("Yo soy", my_age - age, "años mayor que tu")

a = int(input("Introduzca numero: "))
b = int(input("Introduzca numero: "))
if a > b:
    print(a, "es mayor que", b)
elif a < b:
    print(a, "es menor que", b)
else:
    print("Ambos numeros son iguales")





score = int(input("Enter score: "))

grades = {}
for i in range(90, 101):
    grades[i] = 'A'
for i in range(70, 90):
    grades[i] = 'B'
for i in range(60, 70):
    grades[i] = 'C'
for i in range(50, 60):
    grades[i] = 'D'
for i in range(0, 50):
    grades[i] = 'F'

print("Calificación:", grades[score])


month = input('Introduzca mes: ').title()
if month in ["Septiembre", "Octubre", "Noviembre"]:
    print("Otoño")
if month in ["Diciembre", "Enero", "Febrero"]:
    print("invierno")
if month in ["Marzo", "Abril", "Mayo"]:
    print("Primavera")
else:
    print("Summer")

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Introduce fruta: ')
print('Esa fruta ya existe en la lista' if fruit in fruits else fruits.append(fruit))
print(fruits)
