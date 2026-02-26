# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код

# def triangle(point, angle, lenght):
#     for _ in range(3):
#         v = sd.get_vector(start_point=point, angle=angle, length=lenght)
#         v.draw()
#         angle += 120
#         point = v.end_point
        
# def square(point, angle, lenght):
#     for _ in range(4):
#         v = sd.get_vector(start_point=point, angle=angle, length=lenght)
#         v.draw()
#         angle += 90
#         point = v.end_point

# def pentagon(point, angle, lenght):
#     for _ in range(5):
#         v = sd.get_vector(start_point=point, angle=angle, length=lenght)
#         v.draw()
#         angle += 72
#         point = v.end_point

# def hexagon(point, angle, lenght):
#     for _ in range(6):
#         v = sd.get_vector(start_point=point, angle=angle, length=lenght)
#         v.draw()
#         angle += 60
#         point = v.end_point
    
# triangle(sd.get_point(100, 100), 20, 100)
# square(sd.get_point(400,100), 20, 100)
# pentagon(sd.get_point(100,400), 20, 100)
# hexagon(sd.get_point(400,370), 20, 100)

def draw_shape(point, angle, length, sides):
    angle_ratation = 360 / sides
    for _ in range(sides):
        v = sd.get_vector(start_point=point, angle=angle, length=length)
        v.draw()
        angle += angle_ratation
        point = v.end_point



def triangle(point, angle, length):
    draw_shape(point, angle, length, sides=3)

def square(point, angle, length):
    draw_shape(point, angle, length, sides=4)

def pentagon(point, angle, length):
    draw_shape(point, angle, length, sides=5)
    
def hexagon(point, angle, length):
    draw_shape(point, angle, length, sides=6)

triangle(point=sd.get_point(100, 100), angle=20, length=100)
square(point=sd.get_point(400,100), angle=20, length=100)
pentagon(point=sd.get_point(100,400), angle=20, length=100)
hexagon(point=sd.get_point(400,370), angle = 20, length=100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
