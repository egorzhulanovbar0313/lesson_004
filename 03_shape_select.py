# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

# TODO здесь ваш код

def draw_shape(point, angle, length, sides):
    angle_ratation = 360 / sides
    for _ in range(sides):
        v = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
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

shape_list = ['треугольник', 'квадрат', 'пятиугольник', 'шестиугольник']
shape_dict = {
    0: triangle,
    1: square,
    2: pentagon,
    3: hexagon
}

print('Возможные фигуры: ')
for i, value in enumerate(shape_list):
    print(f'{i} : {value}')

while True: 
    user_input = int(input('Введите номер фигуры: '))
    if user_input in shape_dict:
        shape_dict[user_input](point=sd.get_point(250, 250), angle=0, length=150)
        break
    else: print('Введите корректный номер фигуры!')

sd.pause()
