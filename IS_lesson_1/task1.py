# task1
duration = int(input('Введите время в секундах: '))
days = duration // (60 * 60 * 24)
hours = (duration - days * (60 * 60 * 24)) // (60 * 60)
minutes = (duration - days * (60 * 60 * 24) - hours * (60 * 60)) // 60
seconds = duration - days * (60 * 60 * 24) - hours * (60 * 60) - minutes * 60

if duration < 60:
    print(duration, 'сек')
elif minutes < 60 and hours == 0 and days == 0:
    print(minutes, 'мин', seconds, 'сек')
elif hours < 24 and days == 0:
    print(hours, 'час', minutes, 'мин', seconds, 'сек')
else:
    print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
