# from threading import Event


# event = Event()
# # поток клиента может подождать пока флажок будет установлен
# event.wait()
# # серверный поток может установить или сбросить флажок
# event.set()
# event.clear()


import time
from threading import Thread, Event, get_ident
event = Event()
variable = ""


def producer():
    event.set()
    global variable
    variable += "Big data is my best skill!"
    print("Producer говорит: Все ждите пока я работаю")
    time.sleep(5)


def consumer(thread_id):
    while True:
        event.wait()
        print("{} - Я взял. Вот что там было: {}".format(thread_id, variable))


if __name__ == "__main__":
    threads = (Thread(target=consumer, args=(thread_id, ))
               for thread_id in range(10))
    producer()
    for t in threads:
        t.start()
    event.clear()
