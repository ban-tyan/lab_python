
# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["Мама","Папа","Брат","Дедушка","Бабушка"]


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    [my_family[0],160],
    [my_family[1],180],
    [my_family[2],170],
    [my_family[3],160],
    [my_family[4],150],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print(f"Рост отца - {my_family_height[1][1]} см")
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
print(f"Общий рост моей семьи - {sum([my_family_height[x][1] for x in range(len(my_family_height))])} см")
