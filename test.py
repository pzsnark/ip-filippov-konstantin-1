import random

i = 1
lst = []
while i < 45:
    lst.append(random.randint(1, 90))
    i += 1

lst2 = random.sample(lst, 15)

# print(lst)
# print(lst2)


card = [['  '] * 9] * 3
for n in card[0]:
    pass

for element in card:
    print(element)
