numbers = [5,2,1,7,4]
numbers.append(20)
numbers.insert(0,77)
numbers.clear()
numbers = [1,2,1,1]
numbers.pop()
print(numbers)
print(numbers.index(1))
print(5 in numbers)
print(numbers.count(1))
numbers.sort()
numbers.reverse()
numbers2 = numbers.copy()
numbers.append(10)
print(numbers)
print(numbers2)


number = [2,2,4,6,3,4,6,1]
unique = []
for num in number:
     if num not in unique:
         unique.append(num)
print(unique)