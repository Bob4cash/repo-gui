# task2-3: решение задачи без создания нового списка
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
           'была', '+5', 'градусов']

index = 0
while index < len(my_list):
    if my_list[index].isdigit():
        my_list.insert(index, '"')
        my_list[index + 1] = f'{int(my_list[index + 1]):02}'
        my_list.insert(index + 2, '"')
        index += 2

    elif (my_list[index].startswith('+') or my_list[index].startswith('-')) and \
            my_list[index][1:].isdigit():
        my_list.insert(index, '"')
        my_list[index + 1] = f'{my_list[index + 1][0]}{int(my_list[index + 1]):02}'
        my_list.insert(index + 2, '"')
        index += 2
    index += 1

out_str = ' '.join(my_list)
print(out_str)
