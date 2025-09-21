"""
Напишите функцию-декоратор, оборачивающую результат другой функции в прямоугольник звездочек.
Пояснение: если декорируемая функция возвращает “Привет”, то декоратор должен изменить вывод на:
Пример 1:
********
*Привет*
********
Пример 2:
****
*23*
****
Пример 3:
**************
*[34, 45, 12]*
**************
"""
from psutil import swap_memory


def func(arg):
    def wrapper(*args, **kwargs):
        len_value = 0 if len(args) == 0 else len(str(args[0]))
        if len_value:
            header = '*' * (len_value + 2)
            body = '*' + str(args[0]) + '*'
            footer = '*' * (len_value + 2)
            return '\n'.join([header, body, footer])

    return wrapper



def func_two(arg1, arg2):
    return f'Output: {arg1.capitalize()} {arg2.upper()}'


func = func(func_two)


# Тестовая часть
print(func('Привет'))
print(func(23))
print(func([34, 45, 12]))
print(func(arg=100))
print(func_two('hello ', 'python'))
