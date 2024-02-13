

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
garden_set = set(garden)
meadow_set = set(meadow)

# выведите на консоль все виды цветов
# TODO здесь ваш код
all_flowers = garden_set.union(meadow_set)
print("Все виды цветов:", all_flowers)

# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
common_flowers = garden_set.intersection(meadow_set)
print("\n""Цветы, растущие и в саду, и на лугу:", common_flowers)

# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
unique_garden_flowers = garden_set.difference(meadow_set)
print("\n""Цветы, растущие только в саду:", unique_garden_flowers)

# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
unique_meadow_flowers = meadow_set.difference(garden_set)
print("\n""Цветы, растущие только на лугу:", unique_meadow_flowers)
