# Задача 3. Вариант 19.
#  Напишите программу, которая выводит имя "Михаил Николаевич Румянцев", и запрашивает его псевдоним. Программа должна сцеплять две эти строки и выводить полученную строку, разделяя имя и псевдоним с помощью тире.

# Tyshlek D.N.
# 18.04.2017

name = "Михаил Николаевич Румянцев"
print(name)
pen_name = input("Введите псевдоним этого человека: ")
print(name + " - " + pen_name)
input("\n\nНажмите Enter для выхода.")