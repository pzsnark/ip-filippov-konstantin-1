import threading
import time


class ClockThread(threading.Thread):
    def __init__(self, interval, daemon=True):
        super().__init__()
        self.daemon = daemon
        self.interval = interval

    def run(self):
        while True:
            print("Thread #{}. Текущее время {}".format(threading.get_ident(), time.ctime()))
            time.sleep(self.interval)


if __name__ == '__main__':
    t = ClockThread(15)
    t.start()