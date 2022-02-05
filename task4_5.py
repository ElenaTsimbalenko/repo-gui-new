d = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('task4_new.txt', 'w', encoding='utf-8') as f2:
    with open('task4.txt', 'r', encoding='utf-8') as f:
        for i in f:
            i = i.split()
            new_file.append(d[i[0]] + ' ' + i[1])
            f2.writelines(new_file)
        print(new_file)


