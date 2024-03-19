import os

def find_files(directory, extension):
    """
    Генератор, который обходит файловую систему в указанном каталоге и возвращает имена файлов с заданным расширением.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                yield os.path.join(root, file)

def rename_file_with_suffix(file_path, suffix):
    """
    Переименовывает файл, добавляя к его имени суффикс.
    """
    base_name, ext = os.path.splitext(file_path)
    new_file_path = f"{base_name}_{suffix}{ext}"
    os.rename(file_path, new_file_path)
    print(f"Переименован файл: {file_path} -> {new_file_path}")

# Пример использования
directory = '/home/maslenok/Загрузки/zzz' # Укажите путь к вашему каталогу
extension = '.txt' # Расширение файлов, которые нужно переименовать
suffix = 'new' # Суффикс для добавления к именам файлов

# Используем map для переименования файлов с добавлением суффикса
list(map(lambda file_path: rename_file_with_suffix(file_path, suffix), find_files(directory, extension)))
 
