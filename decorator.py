from datetime import datetime
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result  # typing вывел строку
    return wrapper  # возвращает декорирующую функцию


# @timeit  # синтактический сахар, тоже что и typing = timeit(typing)
def typing(text):
    """Функция вывода текста"""
    print(text)


a = typing('Hello world')
print(a)
