names = ["Juan", "Carlos", "Luis", "Mariano"]
print(names)
print(names[0])
print(names[-1])
print(names[2:])
print(names[1:3])
print(names[:])

numbers = [1, 5, 3, 7, 10, 14]
max = numbers[0]
for x in numbers:
    if x > max:
        max = x
print(max)