
# num = 1
# while num <= 15:
#     print(num)
#     #инкремент
#     num+=1
#     if num == 10:
#         #оператор break полностью останавливает цикл
#         break

# num = 1
# while num <= 15:
#     #инкремент
#     num+=1
#     if num == 5:
#         #оператор continue пропускает указанную итерацию
#         continue
#
#     print(num)

#цикл for
# for num in range(1,10):
#     if num == 4:
#         continue
#
#     print(num)

#Система автоматического контроля за температурой
import random

temperatures = [random.randint(0,100) for _ in range(1000) ]

over_heat_count = []

for temp in temperatures:
    print(f"Проверка датчика температуры {temp}")

    if temp > 80:
        print(f"Достигнута опасное значение, температура превышает {temp}, остановка работы")
        over_heat_count.append(temp)


print(f"Всего обнаружено перегревов {over_heat_count}")


