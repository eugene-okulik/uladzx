def operation_selector(func):
    def wrapper(first_number, second_number):
        operation = None
        if first_number == second_number:
            operation = '+'
            print('На основании введенных данных выбрана операция "сумма"')
        elif first_number > second_number:
            operation = '-'
            print('На основании введенных данных выбрана операция "вычитание"')
        elif second_number > first_number:
            operation = '/'
            print('На основании введенных данных выбрана операция "деление"')
        elif first_number < 0 or second_number < 0:
            operation = '*'
            print('На основании введенных данных выбрана операция "умножение"')
        return func(first_number, second_number, operation)
    return wrapper


def calc(first_number, second_number, operation):
    if operation == '+':
        return first_number + second_number
    elif operation == '-':
        return first_number - second_number
    elif operation == '*':
        return first_number * second_number
    elif operation == '/':
        return first_number / second_number
    else:
        print('Данная операция не поддерживается')


@operation_selector
def calc_with_selector(first_number, second_number, operation):
    return calc(first_number, second_number, operation)


first_number_enter = float(input('Введите первое число: '))
second_number_enter = float(input('Введите второе число: '))

result = calc_with_selector(first_number_enter, second_number_enter)

# Вывод результата
print("Результат арифметической операции:", result)
