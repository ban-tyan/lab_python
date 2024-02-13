

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код
lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']

table_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']
table_cost1 = store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
table_cost = table_cost+table_cost1

sofa_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']
sofa_cost1 = store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
sofa_cost = sofa_cost+sofa_cost1

chair_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']
chair_cost1 = store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price']
chair_cost2 = store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']
chair_cost = chair_cost + chair_cost1 + chair_cost2

lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')


table_code = goods['Стол']
tables_item = store[table_code][0]
tables_item1 = store[table_code][1]
tables_quantity0 = tables_item['quantity']
tables_quantity1 = tables_item1['quantity']
tables_quantity = tables_item['quantity'] + tables_item1['quantity']

print('Стол -', tables_quantity, 'шт, стоимость', table_cost, 'руб')


sofa_code = goods['Диван']
sofas_item = store[sofa_code][0]
sofas_item1 = store[sofa_code][1]
sofas_quantity0 = sofas_item['quantity']
sofas_quantity1 = sofas_item1['quantity']
sofas_quantity = sofas_item['quantity'] + sofas_item1['quantity']
print('Диван -', sofas_quantity, 'шт, стоимость', sofa_cost, 'руб')

chair_code = goods['Стул']
chairs_item = store[chair_code][0]
chairs_item1 = store[chair_code][1]
chairs_item2 = store[chair_code][2]
chairs_quantity0 = chairs_item['quantity']
chairs_quantity1 = chairs_item1['quantity']
chairs_quantity2 = chairs_item2['quantity']
chairs_quantity = chairs_item['quantity'] + chairs_item1['quantity'] + chairs_item2['quantity']
print('Стул -', chairs_quantity, 'шт, стоимость', chair_cost, 'руб')
