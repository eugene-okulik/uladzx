import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

# Определение базового пути и пути к csv файлу
base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    csv_data = list(file_data)

# Список для данных, которых нет в БД
missing_data = []

for row in csv_data:
    name = row['name']
    second_name = row['second_name']
    group_title = row['group_title']
    book_title = row['book_title']
    subject_title = row['subject_title']
    lesson_title = row['lesson_title']
    mark_value = row['mark_value']

    query = """
    SELECT * FROM students
    JOIN books
    ON students.id = books.taken_by_student_id
    JOIN `groups`
    ON students.group_id = groups.id
    JOIN marks ON students.id = marks.student_id
    JOIN lessons
    ON marks.lesson_id = lessons.id
    JOIN subjets
    ON lessons.subject_id = subjets.id
    WHERE students.name = %s
    AND students.second_name = %s
    AND groups.title = %s
    AND books.title = %s
    AND subjets.title = %s
    AND lessons.title =%s
    AND marks.value = %s
    """

    cursor.execute(query, (name, second_name, group_title, book_title, subject_title, lesson_title, mark_value))

    result = cursor.fetchall()

    if not result:
        missing_data.append(row)

# Вывод строк, которых нет в БД
if missing_data:
    print("Отсутствующие строки из CSV, которых нет в базе данных:")
    for row in missing_data:
        print(row)
else:
    print("Все строки из файла присутствуют в базе данных.")
