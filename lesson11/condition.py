import threading
# создаем рекурсивную блокировку
mutex = threading.RLock

# создаем переменную состояния и связываем с блокировкой
cond = threading.Condition(mutex)