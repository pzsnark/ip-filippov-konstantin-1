# @trace
# def square(x):
#     return x * x
# # =
# def square(x):
#     return x * x
# square = trace(square)

def some_decorator(func):
    def dop_func():
        print("Do something before")
        func()
        print("Do somethings after")
    return dop_func


def some_decorator2(func):
    def dop_func(*args):
        print("Do something")
        return func(*args)
    return dop_func


@some_decorator
def show_some():
    print("Hello")


@some_decorator2
def pow(x, val):
    return x ** val


show_some()
print(pow(2, 4))
print(pow(3, 3))