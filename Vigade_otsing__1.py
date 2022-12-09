from math import * #Исправлено очередность написания

print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => ")) #Добавлена команда float, добавлена скобка и заменены ковычки
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P)
di=a*sqrt(2) #math.sqr -> sqrt
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #Убрана скобка
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #Добавлена команда float
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #Добавлена команда float
S=b*c
print("Ristküliku pindala", S) #Добавлены ковычки
P=2*(b+c) #Добавлен знак *
print("Ristküliku ümbermõõt", P)
di=sqrt(b**2+c**2) #math.sqr -> sqrt, * -> **
print("Ristküliku diagonaal", round(di,1)) #Добавлена скобка
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) #Добавлена команда float
d=2*r #Добавлен знак *
print("Ringi läbimõõt", d) #Добавлен знак ,
S=pi*r**2 #* -> **, убраны скобки
print("Ringi pindala", round(S,2)) #Добавлено 2 (Количество знаков после запятой)
C=2*pi*r #Добавлен знак *, убраны скобки
print("Ringjoone pikkus", round(C,2)) #Добавлено 2 (Количество знаков после запятой)