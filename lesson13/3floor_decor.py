from functools import wraps


def repeat(n=5):
    def _repeat(f):
        @wraps(f)
        def inner(*args, **kwargs):
            for _ in range(n):
                f(*args, **kwargs)
        return inner
    # не забываем ее вернуть
    return _repeat


@repeat(3)
def foo():
    print("Hello")


foo()
