# class WorkerBuilder:
#     def __init__(self,d):
#         for key, value in d.items():
#             setattr(self, key, value)
# worker = WorkerBuilder({"name": "Петр", "surname": "Алексеев", "age": 10})
# worker = WorkerBuilder({"class_number": "1", "test": "Алексеев", "age": 10})
# print(worker.name)
# print(worker.surname)
# print(worker.test)

# AttributeError: 'WorkerBuilder' object has no attribute 'name'

class HousingBuilder:
    def __init__(self, d):
        for key, value in d.items():
            setattr(self, key, value)


worker = HousingBuilder({"name": "Петр", "surname": "Алексеев", "age": 10})
worker2 = HousingBuilder({"name": "Петр", "surname": "Алексеев", "age": 10, "address": {"streetAddress":
                                                                                        "Московское шоссе",
                                                                                        "city": "Peterburg",
                                                                                        "postCatalog": "123123"},
                          "pool": True, "rooms": 12
                          })

print(worker.name)
print(worker2.address)

# для паттерна Builder библиотека abc