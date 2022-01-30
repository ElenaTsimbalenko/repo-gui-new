from sys import argv

script_name = argv
hours_production = argv
rate_per_hour = argv
bonus = argv

print('Имя скрипта: ', script_name)
print('<< Программа расчета заработной платы сотрудника>>')
print('Выработка в часах: ', hours_production)
print('Ставка в час: ', rate_per_hour)
print('Премия: ', bonus)
print((float(hours_production)*float(rate_per_hour)) + float(bonus))

