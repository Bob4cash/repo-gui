# task3
percent_number = int(input('Введите количество процентов: '))
percent_dict = ['процент', 'процента', 'процентов']
percent_list = []
for percent in range(1, percent_number + 1):
    if percent > 20:
        percent = percent % 10
        if percent == 1:
            percent_list.append(percent_dict[0])
        elif 0 < percent <= 4:
            percent_list.append(percent_dict[1])
        else:
            percent_list.append(percent_dict[2])
    else:
        if percent == 1:
            percent_list.append(percent_dict[0])
        elif percent <= 4:
            percent_list.append(percent_dict[1])
        else:
            percent_list.append(percent_dict[2])
for index, word in enumerate(percent_list, start=1):
    print(index, word)
