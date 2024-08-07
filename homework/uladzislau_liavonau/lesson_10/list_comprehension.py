PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

dict_price_list = {
    i.rsplit(' ', 1)[0]: int(i.rsplit(' ', 1)[1][:-1])
    for i in PRICE_LIST.splitlines()
}

print(dict_price_list)
