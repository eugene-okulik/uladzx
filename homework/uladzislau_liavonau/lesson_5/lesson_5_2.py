result_1 = 'результат операции: 42'

result_2 = 'результат операции: 514'

result_3 = 'результат работы программы: 9'

# string #1
# first_separator_index = result_1.index(':')

result_1_separated = result_1[(result_1.index(':')):]
first_summ = int(result_1_separated[2:]) + 10
print(first_summ)

# string #2
# second_separator_index = result_2.index(':')

result_2_separated = (result_2[(result_2.index(':')):])
second_summ = int(result_2_separated[2:]) + 10
print(second_summ)

# string #3
# third_separator_index = result_3.index(':')

result_3_separated = result_3[(result_3.index(':')):]
third_summ = int(result_3_separated[2:]) + 10
print(third_summ)
