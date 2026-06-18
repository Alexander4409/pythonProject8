#Запись и чтение
# with open("memory.txt","w", encoding="utf-8") as file:
#     file.write("Artem_Sinyagin: Любит писать на python\n")
#     file.write("Семен_Трепп: Любит РКН и Мин.Цифры\n")
#
# with open("memory.txt","r", encoding="utf-8") as file:
#     memory = file.read()
#     print(memory)

import random
print("Генерация логов")

events = ["ДОСТУП РАЗРЕШЕН", "ДОСТУП ЗАПРЕЩЕН", "ОШИБКА ДОСТУПА", "КРИТИЧЕСКИЙ СБОЙ", " ", "Двигатель поврежден"]

with open("raw_data.txt", "w", encoding="utf-8") as file:
    for data in range(1,101):
        log_type = random.choice(events)

        if log_type == "ОШИБКА ДОСТУПА":
            log_type = "ошибка доступа"

        file.write(f"Лог № {data}: {log_type}\n")
