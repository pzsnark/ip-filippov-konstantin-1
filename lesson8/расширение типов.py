# Расширяем стандартный класс dict
class my_dict(dict):
# добавляем свой метод
    def new_method(self):
        return "I'm new method"
# ДобавлЯем дополнительный функционал к существующему методу
    def __setitem__(self, key, value):
        print("Setting %r for %r" % (key, value))
        return super().__setitem__(key, value)
m_dict = my_dict({1: 2, 2: 3})
print(m_dict)
# данная операция вызывает метод __setitem__
m_dict["new_key"] = "new_value"
print(m_dict)
print(m_dict.keys())
print(m_dict.new_method())


class MyList(list):
    """
    Список, индексы которого начинаются с 1, а не с 0
    """
    def __getitem__(self, offset):
        print('(Indexing % s at % s)' % (self, offset))
        return list.__getitem__(self, offset - 1)


x = MyList("abc")  # __init__ наследуется из list
print(x)        # __repr__ наследует из списка
print(x[1])     # MyList.__getitem__
print(x[3])     # изменяет поведение метода суперкласса
x.append("spam")
print(x)        # атрибуты унаследованные от суперкласса list
x.reverse()
print(x)