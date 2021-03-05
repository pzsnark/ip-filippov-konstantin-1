import random

# i = 1
# lst = []
# while i < 45:
#     lst.append(random.randint(1, 90))
#     i += 1
#
# lst2 = random.sample(lst, 15)
#
# print(lst)
# print(lst2)

# генерация последовательности без повторов


card = [[], [], []]
rnd = list(range(1, 30))
random.shuffle(rnd)

for x in range(0, 3):
    for y in range(0, 9):
        card[x].append(rnd[(x * 10)+y])
    card[x] = sorted(card[x])



print('--------------------------')
for element in card:
    print(element)
print('--------------------------')

# print(random.sample(card[0], 5))
