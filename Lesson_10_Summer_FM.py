#API - прослойка между двумя разными приложениями для обмена данными
import os
import json
from openai import OpenAI


client = OpenAI (
    base_url= "https://openrouter.ai/api/v1",
    #Вставить апи ключ
    api_key=""
)

def run_agent():
    print("ИИ агент готов к работе, напишите выход если хотите завершить работу")

    messages = [
        {"role": "system",
         'content':"Ты эксперт в области теплоэнергетики, занимаешься расчётами "
                   "и задачами по оптимизации экономических затрат"}
    ]

    while True:
        try:
            user_input = input("Пользователь: ")
            if user_input.lower() in ["выход", "exit", "quit", "e", "q"]:
                print("Остановка работы ИИ агента")
                break

            if not user_input.strip():
                continue

            messages.append({"role": "user", "content": user_input})

            response = client.chat.completions.create(
                model="deepseek/deepseek-chat",
                messages= messages,
                stream=False
            )
            #Безопасный ответ
            if isinstance(response, str):
                print(f"Сервер вернул текст вместо данных: \n {response}\n")
                messages.pop()
                continue
            # если ответ стандартный
            if hasattr(response, "choices") and response.choices:
                agent_reply = response.choices[0].message.content
                print(f'\nАгент: {agent_reply} \n')
                messages.append({"role": "user", "content": agent_reply})
            else:
                print(f"Не типичный формат ответа {response} \n")
                messages.pop()

        except Exception as e:
            print(f'\n произошла ошибка - {e}')

            if "messages" in locals() and len(messages) > 1 and messages[-1]["role"] == "user":
                messages.pop()

run_agent()







