import random


for i in range(3):
    print(random.random())

for x in range(3):
    print(random.randint(10, 20))

members = ['John', 'Juan', 'Maria', 'Saul']
leader = random.choice(members)
print(leader)


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
