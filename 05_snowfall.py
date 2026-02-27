# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код

x_list = []
while len(x_list) < N:
    x_list.append(sd.random_number(0, 600))
y_list = []
while len(y_list) < N:
    y_list.append(sd.random_number(0, 600))
length_list = []
while len(length_list) < N:
    length_list.append(sd.random_number(10, 20))

def snow_fall(x, y, lenghth, color):
    point = sd.get_point(x, y)
    sd.snowflake(center=point, length=lenghth, color=color)

while True:
    sd.start_drawing()
    for i in range(N):
        snow_fall(x_list[i], y_list[i], length_list[i], sd.background_color)
        y_list[i] -= 10
        x_list[i] += sd.random_number(-5, 5)
        snow_fall(x_list[i], y_list[i], length_list[i], sd.COLOR_WHITE)
        if y_list[i] < 20:
            y_list[i] = 600
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


