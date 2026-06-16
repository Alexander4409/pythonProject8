#высокоуровневый язык
#Основные типы данных
# числа
# int - 1 , 33 ,5 ,7
# float - 1.35, 5.4676
# print(type(121))
# print(type(121.4))
# print(f"Hello")
# print(type(True))

#Составные типы данных
# print(f"Hello")
# print(type([1,2,3,3.4,"fdfdfdf",True]))
# print(type({1:3, "name":+76767676}))
# print(type({1,3,2,4,65,"tjtjtj"}))
# print((1,3,2,4,65,"tjtjtj"))

#Нельзя!!!!
# a = 67
# print(a)

# weather = input("состояние погоды?")
#
# if weather == 'дождь':
#     print("Возьми зонт")
# elif weather == "снег":
#     print("Надень куртку")
# elif weather == "град":
#     print("Не выходить")
# else:
#     print("Можно выходить в легкой одежде")

#отбор кандидатов на полет к марсу
name = input("Напишите ваше имя")
age = int(input("Напишите ваш возраст"))
known_python = input("Знакомы ли вы с ЯП питон?")

if age < 18:
    print(f'К сожалению кандидат {name}, не подходит пол возрасту')
elif age > 50:
    print(f'Уважаемый {name}, вы не переживете полет по состоянию здоровья')
else:
    if known_python.lower() == "да":
        print(f'Поздравляю пользователь {name} прошел первичный отбор')
    else:
        print(f'Пользователь {name} без знания ЯП питона на корабле вам будет нечего делать')
