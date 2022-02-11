class Cell:
    def __init__(self, count):
        self.count = int(count)

    def __add__(self, other):
        return f'Число ячеек объединенной клетки: {self.count + other.count}'

    def __sub__(self, other):
        sub = self.count - other.count
        return f'Число ячеек клетки после вычитания составляет: {sub}' if sub > 0 else 'отсутствие'

    def __truediv__(self, other):
        return self.count // other.count

    def __mul__(self, other):
        return self.count * other.count

    def make_order(self, row):
        result = ''
        for i in range(int(self.count / row)):
            result += '*' * (self.count % row) + '\n'
            return result

cell = Cell(24)
cell_2 = Cell(2)
print (cell + cell_2)
print (cell - cell_2)
print (cell / cell_2)
print (cell * cell_2)
print (cell.make_order(7))
