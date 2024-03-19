# lab_4

### Задача 1. Алгоритм
1. Внутри collect_args создается пустой список args.
2. `def collect_args()` возвращает функцию wrapper.
3. `def wrapper(x):` принимает аргумент x. Внутри нее проверяется условие, если x равно 10:
    - `a = args.copy()` - создается копия списка args и сохраняется в переменной a.
    - `args.clear()` - список args очищается.
    - `return a` - возвращается копия списка, который был собран до этого момента.
4.В противном случае (x не равно 10), аргумент x добавляется в список `args` с помощью `args.append(x)`, и затем возвращается текущее состояние списка `args`.
5.`collect = collect_args()` - вызов функции `collect_args`, результат сохраняется в переменной `collect`. Теперь `collect` содержит функцию wrapper.
6. Когда вызывается `collect(10)`:
    - Список args очищается.
### Задача 2. Алгоритм
1. `def validate(*predic):` принимает произвольное количество предикатов в виде аргументов.
2. `def decorator(func):` принимает функцию func в качестве аргумента.
3. `def wrapper(*args, **kwargs):` принимает произвольное количество позиционных и именованных аргументов.
4. Внутри `wrapper` происходит итерация по предикатам и аргументам с помощью zip(predic, args). Для каждой пары предикат-аргумент выполняется проверка с помощью `if not dic(arg)`. Если проверка не проходит, выбрасывается исключение ValueError.
5. Если все предикаты пройдены успешно, вызывается функция `func` с переданными аргументами и ключевыми аргументами, и результат возвращается.
6. Функция `decorator` возвращает внутреннюю функцию `wrapper`. Функция `validate` возвращает декоратор `decorator`.
7.  Задаются два предиката: первый проверяет, что значение x больше 0, а второй проверяет, что значение y является строкой.


### Результаты
1. ![Screenshot_20240319_162222](https://github.com/ban-tyan/lab_python/assets/145260845/c2c974f6-27a6-403c-a261-6ba7db91f36d)
2. ![Screenshot_20240319_162412](https://github.com/ban-tyan/lab_python/assets/145260845/6edf03a9-dbf9-4ba3-9317-5353accf923a)

### Материалы
1. https://code-basics.com/ru/languages/python/lessons/predicates
2. https://habr.com/ru/companies/otus/articles/727590/
3. https://pythonworld.ru/osnovy/dekoratory.html
4. https://tproger.ru/translations/demystifying-decorators-in-python
5. https://metanit.com/python/tutorial/2.19.php
6. https://codechick.io/tutorials/python/python-closures
