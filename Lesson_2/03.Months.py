print('Выбор месяца но номеру')
check_months = frozenset(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
months_dict = {'1': 'Январь', '2': 'Февраль', '3': 'Март', '4': 'Апрель', '5': 'Май', '6': 'Июнь', '7': 'Июль',
               '8': 'Август', '9': 'Сенябрь', '10': 'Октябрь', '11': 'Ноябрь', '12': 'Декабрь'}
months_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сенябрь', 'Октябрь', 'Ноябрь',
               'Декабрь']
n = ''
while True:
    n = input('Введите номер месяца: ')
    if n.isdigit() and n in check_months:
        print('Значение по листу: ' + months_list[int(n) - 1])
        print('Значение по словарю: ' + months_dict[n])
        break
    else:
        if n == '':
            break
