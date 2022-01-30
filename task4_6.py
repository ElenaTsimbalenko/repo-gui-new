def gen1():
    a = int(input('Введите число: '))
    from itertools import islice
    from itertools import count

    for i in islice(count(a), 10):
        print(i)

gen1()

def gen2():
    list = [1, 107, None, "tsis_list"]

    from itertools import islice
    from itertools import cycle

    for el in islice(cycle(list), 10):
        print(el)

gen2()


