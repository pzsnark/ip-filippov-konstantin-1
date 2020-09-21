def countdown(n):
    e = 0
    def next():
        nonlocal n, e
        e += 1
        r = n
        n -= 1
        return n
    return next


# пример использования
next = countdown(10)
print(next.__closure__[0].cell_contents)
print(next.__closure__[1].cell_contents)
print("\n")
while True:
    v = next()  # получить следующее значение
    print(v)
    if not v: break

