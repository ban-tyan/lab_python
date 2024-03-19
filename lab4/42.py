def validate(*valids):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for validate, arg in zip(valids, args):
                if not validate(arg):
                    raise ValueError(f"Validation failed: {arg}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Пример использования декоратора validate
@validate(lambda x: x > 0, lambda y: lambda y: isinstance(y, str))
def my_function(x, y):
    return f"x={x}, y={y}"

# Пример вызова функции с корректными аргументами
print(my_function(10, 'hello'))

# Пример вызова функции с некорректными аргументами, что вызовет исключение ValueError
print(my_function(-5, 'world'))
