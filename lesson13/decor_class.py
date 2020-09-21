class Log():
    def __init__(self):
        pass

    # магический метод __call__ позволяет обращаться к объекту класса, как к функции
    def __call__(self, func):
        def decorated(*args, **kwargs):
            res = func(*args, **kwargs)
            print("log: {}({}, {}) = {}".format(func.__name__, args, kwargs, res))
            return res
        return decorated


@Log()
def square(x):
    return x * x


square(4)
