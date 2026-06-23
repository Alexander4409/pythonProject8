import customtkinter as ctk

# ВАЖНО: Настройки темы должны быть на самом верхнем уровне модуля
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

# Храним ссылки на UI элементы для отрисовки строк задач
_task_widgets = {}


def create_app_window():
    """Создает главное окно и базовую разметку."""
    # Создаем окно ПЕРВЫМ делом, до вызова любых методов
    app = ctk.CTk()
    app.title("UX/UI Планировщик (MVC)")
    app.geometry("480x550")
    app.resizable(False, False)

    label_title = ctk.CTkLabel(app, text="Мои Задачи", font=("Arial", 24, "bold"))
    label_title.pack(pady=(25, 15))

    input_frame = ctk.CTkFrame(app, fg_color="transparent")
    input_frame.pack(pady=10, padx=20, fill="x")

    task_entry = ctk.CTkEntry(input_frame, placeholder_text="Что нужно сделать?", width=280)
    task_entry.pack(side="left", padx=(0, 10))

    add_btn = ctk.CTkButton(input_frame, text="Добавить", width=100)
    add_btn.pack(side="left")

    scroll_frame = ctk.CTkScrollableFrame(app, width=420, height=320)
    scroll_frame.pack(pady=20, padx=20, fill="both", expand=True)

    return app, task_entry, add_btn, scroll_frame


def render_task(scroll_frame, task_id, text, on_edit, on_delete):
    """Отрисовывает одну задачу на экране."""
    task_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
    task_frame.pack(fill="x", pady=5, padx=5)

    checkbox = ctk.CTkCheckBox(task_frame, text=text, font=("Arial", 14), width=260)
    checkbox.pack(side="left", anchor="w")

    edit_btn = ctk.CTkButton(
        task_frame,
        text="✏️",
        width=30,
        fg_color="transparent",
        hover_color="#3a3a3a",
        command=lambda: on_edit(task_id)
    )
    edit_btn.pack(side="right", padx=(5, 0))

    delete_btn = ctk.CTkButton(
        task_frame,
        text="❌",
        width=30,
        fg_color="transparent",
        hover_color="#e74c3c",
        command=lambda: on_delete(task_id)
    )
    delete_btn.pack(side="right")

    _task_widgets[task_id] = {
        "frame": task_frame,
        "checkbox": checkbox
    }


def remove_task_from_ui(task_id):
    """Удаляет виджет задачи с экрана."""
    if task_id in _task_widgets:
        _task_widgets[task_id]["frame"].destroy()
        del _task_widgets[task_id]


def update_task_in_ui(task_id, new_text):
    """Обновляет текст в существующем чекбоксе."""
    if task_id in _task_widgets:
        _task_widgets[task_id]["checkbox"].configure(text=new_text)


def show_edit_dialog(current_text):
    """Показывает модальное окно для ввода нового текста."""
    dialog = ctk.CTkInputDialog(text="Измените текст задачи:", title="Редактирование")
    dialog.after(100, lambda: dialog._entry.insert(0, current_text))
    return dialog.get_input()


def get_checkbox_text(task_id):
    """Возвращает текущий текст чекбокса."""
    return _task_widgets[task_id]["checkbox"].cget("text")
