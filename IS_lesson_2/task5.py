# task5
goods = [57.8, 46.51, 97, 645.2, 88, 672.34, 1051, 761.5, 87, 57.8, 46.50]
print(id(goods))
goods.sort()
print(id(goods))

for good in goods:
    rub = int(good)
    kop = (good - rub) * 100
    print(f'{rub} руб {kop:02.0f} коп', end=', ')

print('\nЦены пяти самых дорогих товаров:')
for good in sorted(goods)[::-1][:5]:
    rub = int(good)
    kop = (good - int(good)) * 100
    print(f'{rub} руб {kop:02.0f} коп', end=', ')
