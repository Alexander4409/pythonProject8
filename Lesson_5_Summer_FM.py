import time
import random
import os
import webbrowser
import requests
#
# print("Запуск программы ... ")
# time.sleep(1.5)
#
# print("Анализ системы ... ")
# time.sleep(1)
#
# user_pc_name = os.getlogin()
# print(f"Привет пользователь пк {user_pc_name}, компьютер готов к работе!")
#
# predictions = ["Сегодня отличный день чтобы поучиться программированию",
#                "Вижу огромные перспективы в разработке проекта",
#                "Внимание обнаружена нехватка кофе в организме", ]
#
# while True:
#     question = input(f"Пользователь ПК {user_pc_name}, задавайте вопрос.")
#
#     if question.lower() == "выход":
#         print("...")
#         time.sleep(1)
#         print("До скорой встречи")
#         break
#
#     if question.lower()=="Открой сайт":
#         response = requests.get("https://github.com")
#         print(response.status_code)
#         print(response.text)
#
#     for _ in range(3):
#         time.sleep(3)
#         print(".", end="")
#
#     print("\n")
#
#     answer = random.choice(predictions)
#     print(f"Ответ программы: {answer}")


response = requests.get("https://gitflic.ru/")
print(response.status_code)
print(response.text)

#pip install -i https://mirrors.aliyun.com/pypi/simple/ (Название библиотеки )