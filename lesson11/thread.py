import threading
import time


def clock(interval):
    while True:
        print("Thread #{}. Текущее время {}".format(threading.get_ident(), time.ctime()))
        time.sleep(interval)


if __name__ == "__main__":
    t = threading.Thread(target=clock, args=(5, ))
    threads = (threading.Thread(target=clock, args=(5,)) for _ in range(10))

    # for t in threads:
    #     t.start()

    t.start()
