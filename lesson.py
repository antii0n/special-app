num = str(input('Введите число: '))
count = 0

if num[0] == '0':
    num_point = num.replace('.', '')  # убираем точку из числа меньше 1 и дальше действуем для числа с 0 в начале
    for n in num_point:
        num_remain = num_point.replace(n, '')
        if n == '0':
            count -= 1
            continue
        else:
            break
    num_exp = n + '.' + num_remain.replace('0', '')
    print(f'x = {num_exp} * 10 ** {count}')

else:  # для числа больше 1
    for n in num:
        num_remain = num.replace(n, '')
        if n == 0:
            count += 1
            continue
        else:
            break

    for i in num_remain:
        count += 1
    num_exp = n + '.' + num_remain
    print(f'x = {num_exp} * 10 ** {count}')
