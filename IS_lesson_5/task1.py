# task1-2
max_val = int(input('Введите max число генерации: '))
# max_val = 3
odd_nums_gen = (n for n in range(1, max_val + 1, 2))
idx = 0
while idx < max_val:
    print(next(odd_nums_gen))
    idx += 2
