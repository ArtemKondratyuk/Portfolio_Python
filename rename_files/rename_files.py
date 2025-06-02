import os
import re


# 1. Получаем путь от пользователя
folder_path = input("Enter the path to the folder:").strip()


if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
    print("Error: Invalid folder path.")
    exit()


# 2. Получаем шаблон
template = input("Enter the filename template(use # for numbers):").strip()
 
 
match = re.search(r"(#+)", template)    
if not match:
    print("Error: Template must contain at least one '#' as a placeholder.")
    exit()

placeholder = match.group(1)
digits = len(placeholder)


# 3. Получаем расширение из шаблона (если есть)
_, ext = os.path.splitext(template)
 

# 4. Сортируем файлы в папке
all_files = sorted([
    f for f in os.listdir(folder_path)
    if os.path.isfile(os.path.join(folder_path, f)) 
])

    
# 5. Переименовываем каждый файл
for index, filename in enumerate(all_files, start=1):
    number_str = str(index). zfill(digits)
    new_filename = template.replace(placeholder, number_str)
        


    # Сохраняем исходное расширение, если в шаблоне оно не указано    
    if not ext:
        _, orig_ext = os.path.splitext(filename)
        new_filename += orig_ext
    
    
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_filename)


    os.rename(old_path, new_path)
    print(f"Rename: {filename} -> {new_filename}")


print("All files rename successfully.")

    

