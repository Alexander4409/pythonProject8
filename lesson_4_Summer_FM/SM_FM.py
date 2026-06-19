#Запись и чтение
# with open("memory.txt","w", encoding="utf-8") as file:
#     file.write("Artem_Sinyagin: Любит писать на python\n")
#     file.write("Семен_Трепп: Любит РКН и Мин.Цифры\n")
#
# with open("memory.txt","r", encoding="utf-8") as file:
#     memory = file.read()
#     print(memory)

# import random
# print("Генерация логов")
#
# events = ["ДОСТУП РАЗРЕШЕН", "ДОСТУП ЗАПРЕЩЕН", "ОШИБКА ДОСТУПА", "КРИТИЧЕСКИЙ СБОЙ", " ", "Двигатель поврежден"]
#
# with open("raw_data.txt", "w", encoding="utf-8") as file:
#     for data in range(1,101):
#         log_type = random.choice(events)
#
#         if log_type == "ОШИБКА ДОСТУПА":
#             log_type = "ошибка доступа"
#
#         file.write(f"Лог № {data}: {log_type}\n")

# продолжение работы 19.06.2026, 5 занятие

print("Приступаем к очистке данных...")

error_count = 0

clear_logs = []

#чтение данных
with open("raw_data.txt", "r",  encoding="utf-8") as file:
    for line in file:
        clear_line = line.strip().upper()

        if len(clear_line)<10:
            continue

        if "ОШИБКА" in clear_line or "CБОЙ" in clear_line or "ПОВРЕЖДЁН" in clear_line:
            error_count += 1

        clear_logs.append(clear_line)

with open("clear_logs.txt","w", encoding="utf-8") as output_file:
    output_file.write(f"___Итоговый отчет___\n")
    output_file.write(f'сбои и ошибки - {error_count}\n\n')

    for log in clear_logs:
        output_file.write(log+"\n")

print("Анализ завершен\n"
      f"Найдено {error_count} ошибок.")








