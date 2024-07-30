temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31,
    33, 31, 30, 32, 30, 28, 24, 23
]


temperatures_warm = filter(lambda temp: temp > 28, temperatures)
temperatures_warm_list = list(temperatures_warm)

average_temperature = round(sum(temperatures_warm_list) / len(temperatures_warm_list))

print(f'Максимальная температура из списка: {max(temperatures_warm_list)}')
print(f'Минимальная температура из списка: {min(temperatures_warm_list)}')
print(f'Средняя температура: {average_temperature}')
