
# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение площади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()
# TODO здесь ваш код
pi=3.1415926
def krug(a):
    return pi*(a**2)
print((round(krug(radius))))

# Далее, пусть есть координаты точки
point_1 = (23, 34)
x = 23
y = 34
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42],
# то выведите на консоль True, Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False
# TODO здесь ваш код

if (x**2 + y**2) ** 0.5 <= radius:
    print("true")
else:
    print("false")
# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# TODO здесь ваш код
x = 30
y = 30
if (x**2 + y**2) ** 0.5 <= radius:
    print("true")
else:
    print("false")
# Пример вывода на консоль:
#
# 77777.7777
# False
# False


