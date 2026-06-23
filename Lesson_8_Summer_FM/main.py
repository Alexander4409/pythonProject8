import view
import controller

# 1. Создаем интерфейс
app, task_entry, add_btn, scroll_frame = view.create_app_window()

# 2. Передаем элементы управления в контроллер для связывания логики
controller.init_controller(task_entry, add_btn, scroll_frame)

# 3. Запускаем приложение
app.mainloop()
