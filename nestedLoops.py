for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

numbers = [5, 2, 5, 2, 2]
for count in numbers:
    print("x" * count)

for count in numbers:
    output = " "
    for count2 in range(count):
        output += "x"
    print(output)
