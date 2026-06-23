_tasks = []
_current_id = 0

#возвращение всех задач
def get_all_tasks():
    return _tasks

#Добавление задач
def add_task_data(text):
    global _current_id
    _current_id += 1
    task = {"id":_current_id, "text":text, "completed":False}
    _tasks.append(task)
    return _current_id

#Удаление задачи
def delete_task_data(task_id):
    global _tasks
    _tasks = [t for t in _tasks if t["id"] != task_id]

#Обновление текста задачи
def update_task_text(task_id, new_text):
    for task in _tasks:
        if task['id'] == task_id:
            task["text"] = new_text
            break
