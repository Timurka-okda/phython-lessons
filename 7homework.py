# 1
# a = [2, 7, 21, 9, 33, 13]
# s = 0
# for i in a:
#     s += i
# print(s)

# 2
# s = 9
# a = 0
# while 7 < s < 25:
#     a += s
#     s += 2
# print(a)

# 3
# a = 1
# s = 0
# while a < 7:
#     s += a
#     a += 1
# print(s)

# 4
# Я не знаю прогрессий, они и в гугле какие-то сложные поэтому я не сделал 😥

# 5
# a = [3, 4.5, 6, 7.5, 9]
# for i in a: print(f"Объем куба со стороной {i} составляет {i ** 3} см")

# 6
# import math
#
# r = 2.5
# n = 1
# while n <= 6:
#     print(f"Боковая поверхность {n} куба составляет {2 * math.pi * r}")
#     r += 0.5
#     n += 1

# 7
# Хз 😱

# 8
# s = int(input("Введите сколько вы положите денег под 10% годовых: "))
# a = float(input("Сумма вложения должна быть не меньше: "))
# N = 0.1
# count = 0
# while s < a:
#     b = s + s * 0.1
#     if b <= a:
#         s = b
#         count += 1
#     else:
#         break
# print(f"Вам потребуется {count} лет/год")


# 2.1
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
# if a > b > c:
#     a *= 2
#     b *= 2
#     c *= 2
# else:
#     a -= 1
#     b -= 1
#     c -= 1
#
# print(f"a: {a} \nb: {b} \nc: {c}")

# 2.2
# def max(a, b, c):
#     if b > a and b > c:
#         return b
#     if c > a and c > b:
#         return c
#     else:
#         return a
#
#
# x = int(input("1 сторона: "))
# y = int(input("2 сторона: "))
# z = int(input("3 сторона: "))
#
# if max(x, y, z) ** 2 == y**2 + z**2 or max(x, y, z) ** 2 == x**2 + z**2 or max(x, y, z) ** 2 == x**2 + y**2:
#          print("Прямоугольный")
# else:
#     print("Это не прямоугольный треугольник или вообще не треугольник")

# 2.3
# x = int(input("1 сторона: "))
# y = int(input("2 сторона: "))
# z = int(input("3 сторона: "))
# if (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
#     print("Треугольник равнобедренный")
# else:
#     print("Это не прямоугольный треугольник или вообще не треугольник")

# 2.4
# V_CONST = 120
# H_CONST = 6
# print(f"Скорость ветра не должна превышать {V_CONST} км/ч, а облачность не больше {H_CONST} баллов")
# v = int(input("Скорость ветра: "))
# h = int(input("Облачность: "))
# if v < V_CONST and h < H_CONST:
#     print("Самолет может вылетать")
# else:
#     print("Самолет не может вылетать")

# 2.5
# a = int(input("1 ученик: "))
# b = int(input("2 ученик: "))
# c = int(input("3 ученик: "))
# if a > 5 and b > 5 and c > 5:
#     print("Команда попадает на финальный этап")
# else:
#     print("Команда не попадает на финальный этап")

# 2.6
# a = int(input("1 ученик: "))
# b = int(input("2 ученик: "))
# c = int(input("Нужно набрать не меньше: "))
# if a == b and (a > c and b > c):
#     print("Both")
# elif a > b and a > c:
#     print("First")
# elif b > a and b > c:
#     print("Second")
# elif c > b and c > a:
#     print("None of them, lol")

# 2.7
# import random
# import time
#
# a_dinamo = random.randint(1, 2)
# a_shachtar = random.randint(1, 2)
# dinamo_win = False
# shachtar_win = False
# # ⟨⟨⟩⟩
# if a_dinamo == 1:
#     print("Команда ⟨⟨Динамо⟩⟩ проиграла ⟨⟨Ворскле⟩⟩")
#     time.sleep(0.7)
#     print("Команда ⟨⟨Динамо⟩⟩ не стала чемпионом :(")
# else:
#     print("Команда ⟨⟨Динамо⟩⟩ выиграла ⟨⟨Ворсклу⟩⟩")
#     dinamo_win = True
#     if a_shachtar == 1:
#         print("Команда ⟨⟨Шахтар⟩⟩ проиграла ⟨⟨Днепру⟩⟩")
#         shachtar_win = True
#     else:
#         print("Команда ⟨⟨Шахтар⟩⟩ выиграла ⟨⟨Днепр⟩⟩")
#         time.sleep(0.7)
#         print("Команда ⟨⟨Шахтар⟩⟩ не стала чемпионом :(")
#
#
# if dinamo_win == True and shachtar_win == True:
#     time.sleep(1)
#     print("УРААААААА!! ⟨⟨Динамо⟩⟩ ВЫИГРАЛА!!! ПОЗДРАВЛЯЕМ!!!")
