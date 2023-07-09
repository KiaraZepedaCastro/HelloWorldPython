try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(risk)
except ValueError:
    print('Invalid value')
