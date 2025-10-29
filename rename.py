import os
from tkinter import *
from tkinter import filedialog


def rename_files():
    # Получаем указанный путь к директории
    directory = entry.get()
    if not os.path.exists(directory):
        result_label.config(text="Директория не найдена.", fg="red")
        return

    # Получаем список файлов в директории и сортируем их
    files = sorted([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])

    # Переносим каждый файл в новую нумерацию
    for idx, file in enumerate(files):
        ext = os.path.splitext(file)[1]
        new_filename = f"{idx+1}{ext}"  # Создаем новое имя вида '1.jpg', '2.txt' и т.п.
        old_file_path = os.path.join(directory, file)
        new_file_path = os.path.join(directory, new_filename)

        try:
            os.rename(old_file_path, new_file_path)
        except OSError as err:
            result_label.config(text=f"Ошибка при переименовании файла '{file}': {err}", fg="red")
            return

    result_label.config(text="Все файлы успешно переименованы!", fg="green")


# Интерфейс программы с Tkinter
root = Tk()
root.title("Переименователь файлов")

# Метка и поле ввода пути
label = Label(root, text="Выберите директорию:")
label.pack(pady=10)
entry = Entry(root, width=50)
entry.pack(pady=10)

# Кнопка выбора директории
def browse_dir():
    selected_dir = filedialog.askdirectory()
    entry.delete(0, END)
    entry.insert(0, selected_dir)

browse_button = Button(root, text="Обзор...", command=browse_dir)
browse_button.pack(side=LEFT, padx=(0, 10))

# Кнопка начала переименования
rename_button = Button(root, text="Переименовать файлы", command=rename_files)
rename_button.pack(side=RIGHT, pady=10)

# Поле вывода статуса
result_label = Label(root, text="", fg="black")
result_label.pack(pady=10)

# Запускаем главное окно
root.mainloop()