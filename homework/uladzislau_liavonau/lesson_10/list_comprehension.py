PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_dict = dict(
    map(
        lambda item: (item.rsplit(' ', 1)[0], int(item.rsplit(' ', 1)[1][:-1])),
        PRICE_LIST.splitlines()
    )
)

print(price_dict)
