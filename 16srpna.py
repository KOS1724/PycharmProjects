# try:
#     file = open('./txt/example1.txt', 'r')
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print('Файл не найден')
# finally:
#     print('Завршение работы')
#     try:
#     print('Работа завершена')
#     except NameError:
#     print('-------------------')
#     print('файл не был оькрыт, Работа завершена')


# def check_positive(number):
#     if number <0:
#         raise ValueError('Число отрицательное')
#     else:
#         return number
#
# try:
#     print(check_positive(10))
# except ValueError as e:
#         print(e)


def check_positive(number):
    if number == 0:
        raise ZeroDivisionError('У нас ноль')

a = 10 / 0
try:
    # check_positive(0)
    a = 10 / 0
except ZeroDivisionError as nasheSoobshenie:
    print(f'Возникла ошибка {nasheSoobshenie}')