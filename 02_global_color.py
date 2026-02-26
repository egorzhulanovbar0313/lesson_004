# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# TODO здесь ваш код

#Создаем словари цветов для вывода пользвателю и проверки ввода от пользователя
colors_dict = {0: 'red',
               1: 'orange',
               2: 'yellow', 
               3: 'green',
               4: 'cyan',
               5: 'blue',
               6: 'purple',
               }

colors_map = {0: sd.COLOR_RED,
              1: sd.COLOR_ORANGE,
              2: sd.COLOR_YELLOW, 
              3: sd.COLOR_GREEN,
              4: sd.COLOR_CYAN,
              5: sd.COLOR_BLUE,
              6: sd.COLOR_PURPLE,
               }

#Показываем пользователю возможные цвета и делаем проверку на соответствие
print('Возможные цвета:')
for key, value in colors_dict.items():
    print(f'{key} : {value}')

while True:
    user_input = int(input('Введите номер цвета: '))

    if user_input in colors_map:
        color = colors_map[user_input]
        break
    else:
        print('Вы ввели некоректный номер!')

#Создаем функцию отрисовки фигуры
def draw_shape(point, angle, length, sides):
    angle_ratation = 360 / sides
    for _ in range(sides):
        v = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v.draw(color=color)
        angle += angle_ratation
        point = v.end_point
        


#Создаем функции отрисовки конкретных фигур, которые внутри себя вызывают функцию отрисовки фигуры.
def triangle(point, angle, length):
    draw_shape(point, angle, length, sides=3)

def square(point, angle, length):
    draw_shape(point, angle, length, sides=4)

def pentagon(point, angle, length):
    draw_shape(point, angle, length, sides=5)
    
def hexagon(point, angle, length):
    draw_shape(point, angle, length, sides=6)

#Функции отрисовки конкретных фигур
triangle(point=sd.get_point(100, 100), angle=20, length=100)
square(point=sd.get_point(400,100), angle=20, length=100)
pentagon(point=sd.get_point(100,400), angle=20, length=100)
hexagon(point=sd.get_point(400,370), angle = 20, length=100)

sd.pause()
