def foo():
    x = 13
    array = ["lol", "kek"]
    def helloman():
        print("Привет, мистер{}".format(x))
        print("Вот твой список клиентов: {}".format(array))
    return helloman


bar = foo()
bar()
# посмотрим какие есть аттрибуты у helloman
print(dir(bar))

# если мы посмотрим то увидим, что в замыкании есть два объекта
print(bar.__closure__)
# выведем их
for attr in bar.__closure__:
    print(attr.cell_contents)

# Зададим ссылку. array2 ссылается на тот же объект в памяти?
array2 = bar.__closure__[0].cell_contents
# проверим. Добавим еще один элемент в массив и выполним функцию еще раз
array2.append("cheburek")
bar()
