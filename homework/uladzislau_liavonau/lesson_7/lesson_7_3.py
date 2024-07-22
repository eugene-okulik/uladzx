result_1 = 'результат операции: 42'

result_2 = 'результат операции: 54'

result_3 = 'результат работы программы: 209'

result_4 = 'результат: 2'


def result_funct(result):
    result_separated = result[(result.index(':')):]
    summ = int(result_separated[2:]) + 10
    print(summ)


result_funct(result_1)
result_funct(result_2)
result_funct(result_3)
result_funct(result_4)
