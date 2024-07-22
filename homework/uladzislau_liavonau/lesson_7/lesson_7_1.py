program_value = 66

user_input = int(input(f'Введите число: '))

while user_input != program_value:
    print("Попробуйте cнова")
    user_input = int(input(f'Введите число: '))

print("Поздравляю! Вы угадали")
