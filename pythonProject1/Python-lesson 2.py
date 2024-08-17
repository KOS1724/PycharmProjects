# a=True
# b=False

# print(a and b)
# print(a or b)
# print(not a)


# username = 'user'
# password = 'pass'

# input_username = input('Enter login ')
# input_password = input('Enter password ')

# is_username_correct = input_username == username
# is_password_correct = input_password == password

# if is_username_correct and is_password_correct:
#     print('Dostup razresen')
# else:
#     print('Dostup zapresen')

# age = int(input("Введите ваш возраст: "))
# if age < 18:
#     print('Вы несовершеннолетний.')
# elif age < 65:
#     print('Vy vzroslyj')
# else:
#     print('Vy pensioner')



# score=int(input("Vvedite Vas scet: "))

# if score>=100:
#     print("Vy vzhrali!')
# else:
#     print("Vy proihrali!(")

# a=10
# b=3
# if age  a>b:
#     remainder=a%b



a = int(input("Vvedite pervoe cislo: "))
b = int(input("Vvedite vtoroe cislo: "))
operacion = input('+,-,*,/: ')


if operacion == '+':
    result = a + b
    print(f"{a}+{b}={result}")
elif operacion == '-':
    result = a - b
    print(f"{a}-{b}={result}")
elif operacion == '*':
    result = a * b
    print(f"{a}*{b}={result}")
elif operacion == '/':
    if b != 0:
        result = a / b
    print(f"{a}/{b}={result}")
else:
    print('Na nol delit nelza')