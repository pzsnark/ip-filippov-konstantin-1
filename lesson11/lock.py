# from threading import Lock
#
#
# lock = Lock()
# lock.acquire()
# # ... код внутри блокировки
# lock.release()


import threading


protected_resource = 0
unprotected_resource = 0

NUM = 500000
mutex = threading.Lock()


def safe_plus():
    """потокобезопасный инкремент"""
    global protected_resource
    for i in range(NUM):
        # ставим блокировку
        mutex.acquire()
        protected_resource += 1
        mutex.release()


def safe_minus():
    """потокобезопасный декремент"""
    global protected_resource
    for i in range(NUM):
        # ставим блокировку
        mutex.acquire()
        protected_resource -= 1
        mutex.release()


def risky_plus():
    """инкремент без блокировки"""
    global unprotected_resource
    for i in range(NUM):
        unprotected_resource += 1


def risky_minus():
    """декремент без блокировки"""
    global unprotected_resource
    for i in range(NUM):
        unprotected_resource -= 1


if __name__ == "__main__":
    thread1 = threading.Thread(target=safe_plus)
    thread2 = threading.Thread(target=safe_minus)
    thread3 = threading.Thread(target=risky_plus)
    thread4 = threading.Thread(target=risky_minus)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    print("Результат при работе с блокировкой %s" % protected_resource)
    print("Результат при работе без блокировкой %s" % unprotected_resource)