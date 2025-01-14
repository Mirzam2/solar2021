# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
from solar_vis import DrawableObject
import json


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем

            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_unit_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_unit_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return [DrawableObject(obj) for obj in objects]


def parse_unit_parameters(line, unit):
    """Считывает данные о звезде из строки.

    Входная строка должна иметь слеюущий формат:

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.

    Пример строки:

    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.

    **star** — объект звезды.
    """
    line_fix = line.split()
    unit.R = float(line_fix[1])
    unit.color = line_fix[2]
    unit.m = float(line_fix[3])
    unit.x = float(line_fix[4])
    unit.y = float(line_fix[5])
    unit.Vx = float(line_fix[6])
    unit.Vy = float(line_fix[7])


def write_space_objects_data_to_file(output_filename, list):
    """Сохраняет данные о космических объектах в файл.
    **output_filename** — имя входного файла
    **list** — список данных которые нужно сохранить
    """
    with open(output_filename, 'w') as out_file:
        json.dump(list, out_file)

def saving_data_to_an_list(list,space_object,main_object,time):
    """Сохраняет данные о звездах в массив
    list - массив в которой надо
    space_objects - данные чего нужно сохранять
    """
    v = (space_object.obj.Vx ** 2 + space_object.obj.Vy ** 2)**0.5
    r = ((space_object.obj.x - main_object.obj.x) ** 2 + (space_object.obj.y - main_object.obj.y) ** 2) ** 0.5 * 10 ** (-10)
    list = list.append([time, v, r])

if __name__ == "__main__":
    print("This module is not for direct call!")
