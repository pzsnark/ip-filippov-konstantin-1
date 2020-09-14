import json
import time
from threading import Thread, Lock, RLock

lock = Lock()

people_from_first_db = [
    {
        "firstName": "Ilon",
        "lastName": "Mask",
        "age": 48
    },
    {
        "firstName": "Alan",
        "lastName": "Turing",
        "age": 41
    }
]

people_output = []


def write_json():
    lock.acquire()
    with open("dump.json", "w") as fp:
        json.dump({"people": people_from_first_db}, fp)
    lock.release()


def get_first_part():
    lock.acquire()
    first_part = {}
    with open("dump.json", "r") as fp:
        data = json.load(fp)
        people = data.get("people", [])
        if people:
            try:
                first_part = people[0]
            except (IndexError, ValueError) as ex:
                # файл не соответствует условиям
                pass
    lock.release()
    return first_part


def get_second_part():
    lock.acquire()
    second_part = {}
    with open("dump.json", "r") as fp:
        data = json.load(fp)
        people = data.get("people", [])
        if people:
            try:
                second_part = people[1]
            except (IndexError, ValueError) as ex:
                # файл не соответствует условиям
                pass
    lock.release()
    return second_part


def get_both_parts():
    while people_output != people_from_first_db:
        lock.acquire()
        first = get_first_part()
        if first:
            people_output.append(first)
        second = get_second_part()
        if people_output and second:
            people_output.append(second)
        lock.release()
        time.sleep(3)


if __name__ == "__main__":
    t1 = Thread(target=write_json(), daemon=True)
    t2 = Thread(target=get_both_parts(), daemon=True)
    t3 = Thread(target=get_both_parts(), daemon=True)
    t2.start()
    t3.start()
    time.sleep(5)
    print(people_output)
