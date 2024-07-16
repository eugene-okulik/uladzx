result_1 = 'результат операции: 42'

result_2 = 'результат операции: 514'

result_3 = 'результат работы программы: 9'

# string #1

first_number = int(result_1[(result_1.index('42')):]) + 10

print(first_number)

# string #2

second_number = int(result_2[(result_2.index('514')):]) + 10

print(second_number)

# string #3

third_number = int(result_3[(result_3.index('9')):]) + 10

print(third_number)
