#Функции
# def - определение
# Процедура
# def say_hi(name, age):
#     print(f"Привет {name} !")
#     print(f"Твой возраст - {age}")
#
# name = input("Как тебя зовут?")
# say_hi(name,67)
#
# Функция с оператором return
# def greetings():
#     name = input("Напиши свое имя")
#     age = int(input("Напиши свой возраст"))
#     return f"Привет {name}, тебе сейчас {age}, но через 10 лет твой возраст будет {age+10}"
#
#
#
# print(greetings())

# def summ(*args):
#     result = 0
#     for num in args:
#         result += num
#     return f'сумма чисел переданных в функцию = {result}'
#
#
# summ_element = summ(1,2,4,2,4,623,6,9,54,9,3)
#
# print(summ_element)
#customTkinter ___Дизаин___
# UX - пользовательский опыт (Решить задачу пользователя максимально быстро и комфортно)
# UI - Пользовательский интерфейс


#Простое окно с кнопкой
# import customtkinter as ctk
#
# ctk.set_appearance_mode("System")
# ctk.set_default_color_theme("green")
#
# app = ctk.CTk()
# app.geometry("500x400")
# app.title("Тестовое окно 500 на 400 пикселей")
#
# def clik():
#     print("Вы нашали на кнопку")
#
# btn = ctk.CTkButton(master=app, text="Нажми меня!", command=clik)
# btn.pack(pady=20)
#
# app.mainloop()


#Задачник


import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

#Функция добавления и управления задачами
def add_task():
    #Добавление задачи
    task_text = task_entry.get().strip()
    if task_text:
        task_frame = ctk.CTkFrame(scroll_fame,fg_color="transparent")
        task_frame.pack(fill="X", pady=5, padx=5)

    #Чекбокс
        checkbox = ctk.CTkCheckBox(task_frame, text=task_text, font=("Arial",14), width=250)
        checkbox.pack(side ="left", anchor="w")
    #Редактирование задачи
        edit_btn = ctk.CTkButton(
            task_frame,
            text="✏️",
            width=30,
            fg_color="transparent",
            hover_color="#3a3a3a",
            command=lambda cb=checkbox: edit_task(cb))



# https://www.figma.com/design/1f60xMtb9YZpdyDD0OEgsN/Landify---Landing-Page-UI-Kit--Community---Copy-?node-id=719-0&p=f&t=0wcQen0HgbFuEtrc-0
# https://github.com/tomschimansky/customtkinter