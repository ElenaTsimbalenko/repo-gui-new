with open('task3.txt', 'r', encoding='utf-8') as my_file:
    names = []
    aver_income = 0
    num = 0
    for line in my_file:
        num += 1
        name, income = (i for i in line.split())
        income = float(income)
        if income < 20000:
            names.append(name)
        aver_income += income
    salary = aver_income/num
print(*names)
print(round(salary))



