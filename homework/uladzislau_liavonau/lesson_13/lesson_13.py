import os
from datetime import datetime, timedelta

# Определяем базовый путь и путь к файлу
base_path = '/Users/uladzislauliavonau/QA_Automation_course/uladzx/homework/eugene_okulik/hw_13/'
file_path = os.path.join(base_path, 'data.txt')


# Генератор для работы со строками в файле
def read_file(input_path):
    with open(input_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line


# Форматирование строк файла согласно требований
def modified_data_line(data_line):
    date_object = datetime.strptime(data_line[3:29], "%Y-%m-%d %H:%M:%S.%f")

    if '1.' in data_line:
        return f'Дата на неделю позже: {date_object + timedelta(days=7)}'
    elif '2.' in data_line:
        return f"День недели для даты: {date_object} - это {date_object.strftime('%A')}"
    else:
        current_date = datetime.now()
        days_delta = (current_date - date_object).days
        return f"{date_object} дата была {days_delta} дней назад"


for file_line in read_file(file_path):
    result = modified_data_line(file_line)
    print(result)
