# lab_4

### Задача 1. Алгоритм
1. Функция `find_files` представляет собой генератор, который обходит файловую систему в указанном каталоге и возвращает имена файлов с заданным расширением.
  - `os.walk(directory)` возвращает кортежи `(root, dirs, files)` для каждого каталога внутри `directory`.
  - Цикл `for file in files` проходит по всем файлам в текущем каталоге.
  - Условие `if file.endswith(extension)` фильтрует файлы по заданному расширению.
  - `yield os.path.join(root, file)` возвращает полный путь к найденному файлу.
2. Функция `rename_file_with_suffix` принимает путь к файлу `file_path` и суффикс `suffix`, добавляя его к имени файла при переименовании.
3. `os.path.splitext(file_path)` разделяет путь к файлу на базовое имя и расширение. Создается новый путь `new_file_path`, объединяя базовое имя с суффиксом и старым расширением.
4. `os.rename(file_path, new_file_path)` переименовывает файл, заменяя его на новое имя.
5. `list(map(lambda file_path: rename_file_with_suffix(file_path, suffix), find_files(directory, extension)))`
 Вызывается rename_file_with_suffix для каждого найденного файла из find_files.Полученный результат обернут в list, чтобы активировать выполнение map.


### Результаты
![Screenshot_20240319_190833](https://github.com/ban-tyan/lab_python/assets/145260845/522270b0-fc69-4820-874d-47b8fd72098d)


### Материалы
https://realpython.com/python-map-function/
https://skillbox.ru/media/code/generatory_python_chto_eto_takoe_i_zachem_oni_nuzhny/
https://wiki.python.org/moin/Generators
https://www.programiz.com/python-programming/generator
https://habr.com/ru/articles/560300/
