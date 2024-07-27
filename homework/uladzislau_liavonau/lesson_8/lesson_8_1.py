import random

salary = int(input('Введите salary: '))

bonus_T_or_F = random.choice([True, False])

bonus_rndm = int(random.random() * 100)
print(f'Бонус равен: {bonus_rndm}')

if bonus_T_or_F:
    print(salary, bonus_T_or_F, f"-'${salary + bonus_rndm}'")
else:
    print(salary, bonus_T_or_F, f"-'${salary}'")
