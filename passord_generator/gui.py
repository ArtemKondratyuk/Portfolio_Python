import ttkbootstrap as ttkb
from ttkbootstrap.constants import PRIMARY  # Настройка внешнего вида интерфейса
from generator import password_generator  # Функция генерации пароля


def run_gui():
    root = ttkb.Window(themename="superhero")  # Варианты тем интерфейсов: "darkly", "solar", "cyborg", "superhero"

    root.geometry("600x250")  # Размер окна
    root.resizable(False, False)  # Запрет для Пользователя на изменение размера окна
    root.title("Password Generator")  # Название окна

    # 1. Фрейм для настроек чекбоксов.
    main_frame = ttkb.Frame(root)
    main_frame.grid(row=0, column=0, padx=(80, 10), pady=10)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Флажки (галочки)
    use_uppercase = ttkb.BooleanVar(value=True)
    use_lowercase = ttkb.BooleanVar(value=True)
    use_digits = ttkb.BooleanVar(value=True)
    use_symbols = ttkb.BooleanVar(value=True)

    ttkb.Label(main_frame, text="Settings", font=("Arial", 13)).grid(
        row=0, column=0, columnspan=2, sticky="w", padx=110, pady=(0, 10)
    )

    style = ttkb.Style()
    style.configure("Custom.TCheckbutton", font=("Arial", 11))

    ttkb.Checkbutton(main_frame, text="Big letters", variable=use_uppercase, style="Custom.TCheckbutton").grid(
        row=1, column=0, sticky="w", padx=10, pady=2
    )
    ttkb.Checkbutton(main_frame, text="Small letters", variable=use_lowercase, style="Custom.TCheckbutton").grid(
        row=2, column=0, sticky="w", padx=10, pady=2
    )
    ttkb.Checkbutton(main_frame, text="Numbers", variable=use_digits, style="Custom.TCheckbutton").grid(
        row=1, column=1, sticky="w", padx=10, pady=2
    )
    ttkb.Checkbutton(main_frame, text="Symbols", variable=use_symbols, style="Custom.TCheckbutton").grid(
        row=2, column=1, sticky="w", padx=10, pady=2
    )

    # 2. Фрейм для длины пароля (метка + выпадающий список).
    length_frame = ttkb.Frame(main_frame)
    length_frame.grid(row=3, column=0, columnspan=2, pady=(10, 5))

    ttkb.Label(length_frame, text="Password length:", font=("Arial", 12)).pack(side="left", padx=5)

    length_var = ttkb.StringVar(value="8")
    length_combobox = ttkb.Combobox(
        length_frame,
        textvariable=length_var,
        values=[str(i) for i in range(8, 21)],
        width=5,
        state="readonly",
        font=("Arial", 12),
    )
    length_combobox.pack(side="left", padx=5)

    # Кнопка генерации и поле вывода.
    def generate_password():
        try:
            # Получаем параметры из интерфейса.
            length = int(length_var.get())
            include_upper = use_uppercase.get()
            include_lower = use_lowercase.get()
            include_digits = use_digits.get()
            include_symbols = use_symbols.get()

            # Генерация пароля.
            password = password_generator(
                length=length,
                use_uppercase=include_upper,
                use_lowercase=include_lower,
                use_digits=include_digits,
                use_symbols=include_symbols,
            )

            # Отображение в поле.
            password_output.delete(0, "end")
            password_output.insert(0, password)

        except ValueError:
            # Показываем сообщение в случае ошибки
            password_output.delete(0, "end")
            password_output.insert(0, "Error")

    # Копирование пароля.
    def copy_password():
        root.clipboard_clear()
        root.clipboard_append(password_output.get())

    # 3. Фрейм для поля и кнопки копирования.
    password_frame = ttkb.Frame(main_frame)
    password_frame.grid(row=4, column=0, columnspan=2, pady=(15, 0))

    password_output = ttkb.Entry(password_frame, width=30, justify="center", font=("Arial", 12))
    password_output.grid(row=0, column=0, padx=(0, 10))

    copy_btn = ttkb.Button(password_frame, text="Copy", width=5, command=copy_password, bootstyle="info-outline")
    copy_btn.grid(row=0, column=1)

    # Кнопка генерации пароля — центр под полем
    generate_btn = ttkb.Button(
        main_frame, text="Get a password", command=generate_password, bootstyle=PRIMARY
    )
    generate_btn.grid(row=5, column=0, columnspan=2, pady=(10, 0), ipadx=10, sticky="w", padx=90)

    # Настройки появления окна после запуска приложения
    # Окно появляется по середине экрана с небольшим смещением вверх
    window_width = 600
    window_height = 250

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    offset_y = int(screen_height * 0.2)

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2) - offset_y

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.mainloop()


if __name__ == "__main__":
    run_gui()
