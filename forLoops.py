for item in "Python":
    print(item)

for item in ["Mosh", "Juan", "Luis"]:
    print(item)

for item in [1, 7, 3, 4, 10]:
    print(item)

for item in range(10):
    print(item)

for item in range(5,10):
    print(item)

for item in range(5, 10, 2):
    print(item)

prices = [10, 20, 30]
total = 0
for items in prices:
    total += items
print(f"Total: {total}")