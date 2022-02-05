from random import randint

with open('task5.txt', 'w', encoding='utf-8') as f:
    my_list = [randint(1, 100) for _ in range(100)]
    f.write(' '.join(map(str, my_list)))

with open('task5.txt', 'r', encoding='utf-8') as f2:
    numbers = [int(i) for i in f2.read().split()]
    print(sum(numbers))






