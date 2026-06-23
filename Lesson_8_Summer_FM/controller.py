import model
import view

# Глобальные ссылки на элементы ввода, которые мы получим при старте
_task_entry = None
_scroll_frame = None


def handle_add_task():
    """Логика добавления задачи."""
    text = _task_entry.get().strip()
    if text:
        # 1. Обновляем модель (данные)
        task_id = model.add_task_data(text)

        # 2. Обновляем отображение (интерфейс)
        view.render_task(
            _scroll_frame,
            task_id,
            text,
            on_edit=handle_edit_task,
            on_delete=handle_delete_task
        )

        # Очищаем поле ввода
        _task_entry.delete(0, 'end')


def handle_delete_task(task_id):
    """Логика удаления задачи."""
    # 1. Удаляем из данных
    model.delete_task_data(task_id)
    # 2. Удаляем из UI
    view.remove_task_from_ui(task_id)


def handle_edit_task(task_id):
    """Логика редактирования задачи."""
    current_text = view.get_checkbox_text(task_id)
    new_text = view.show_edit_dialog(current_text)

    if new_text and new_text.strip():
        clean_text = new_text.strip()
        # 1. Обновляем модель
        model.update_task_text(task_id, clean_text)
        # 2. Обновляем UI
        view.update_task_in_ui(task_id, clean_text)


def init_controller(task_entry, add_btn, scroll_frame):
    """Инициализирует связи контроллера с UI элементами."""
    global _task_entry, _scroll_frame
    _task_entry = task_entry
    _scroll_frame = scroll_frame

    # Назначаем команду для главной кнопки добавления
    add_btn.configure(command=handle_add_task)
