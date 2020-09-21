from urllib.request import urlopen


def page(url):
    def get():
        return urlopen(url).read()
    return get


python = page("http://www.python.org")
jython = page("http://www.jython.org")
# какой то другой код
# ...
# в нужном месте вызываем
pydata = python()
jydata = jython()
print(pydata[:64])
print(jydata[:64])
print(python.__closure__)
print(python.__closure__[0].cell_contents)  # url до сих пор доступна
