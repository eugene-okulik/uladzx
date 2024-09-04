import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)


class Student:
    def __init__(self, name, second_name):
        self.name = name
        self.second_name = second_name

    def query_to_add_student(self):
        query_to_add_student = 'INSERT INTO students(name, second_name) VALUES (%s, %s)'
        cursor.execute(query_to_add_student, (self.name, self.second_name))
        student_id_from_db = cursor.lastrowid
        return student_id_from_db


class Book:
    def __init__(self, book_name, student_id):
        self.book_name = book_name
        self.student_id = student_id

    def query_to_add_book(self):
        query_to_add_book = 'INSERT INTO books(title, taken_by_student_id) VALUES (%s, %s)'
        cursor.execute(query_to_add_book, (self.book_name, self.student_id))
        book_id_from_db = cursor.lastrowid
        return book_id_from_db


class Group:
    def __init__(self, group_title, student_id):
        self.group_title = group_title
        self.student_id = student_id
        self.group_id = None

    def add_group_and_assign_student(self):
        # Создаем группу и получаем ее ID
        query_to_add_group = 'INSERT INTO `groups`(title) VALUES (%s)'
        cursor.execute(query_to_add_group, (self.group_title,))
        self.group_id = cursor.lastrowid

        # Обновляем запись студента, присваивая ему group_id
        query_to_add_student_to_group = 'UPDATE students SET group_id = %s WHERE id = %s'
        cursor.execute(query_to_add_student_to_group, (self.group_id, self.student_id))
        return self.group_id


class Subject:
    def __init__(self, subject_title):
        self.subject_title = subject_title

    def query_to_add_subject(self):
        # Создаем предмет и получаем его ID
        query_to_add_subject = 'INSERT INTO subjets (title) VALUES (%s)'
        cursor.execute(query_to_add_subject, (self.subject_title,))
        subject_id_from_db = cursor.lastrowid
        return subject_id_from_db


class Lesson:
    def __init__(self, lesson_title, subject_id):
        self.lesson_title = lesson_title
        self.subject_id = subject_id

    def query_to_add_lesson(self):
        # Создаем занятие и получаем его ID
        query_to_add_lesson = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
        cursor.execute(query_to_add_lesson, (self.lesson_title, self.subject_id))
        lesson_id_from_db = cursor.lastrowid
        return lesson_id_from_db


class Mark:
    def __init__(self, mark_value, lesson_id, student_id):
        self.mark_value = mark_value
        self.lesson_id = lesson_id
        self.student_id = student_id

    def query_to_add_mark_to_lesson(self):
        # Проставляем оцентку для предмета и возвращаем её ID
        query_to_add_mark_to_lesson = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
        cursor.execute(query_to_add_mark_to_lesson, (self.mark_value, self.lesson_id, self.student_id))
        mark_id_from_db = cursor.lastrowid
        return mark_id_from_db


# 1.Создайте студента (student):
student = Student('Lionel', 'Messi')
student_db_id = student.query_to_add_student()  # Получаем ID студента

print(f"ID добавленного студента {student.name} {student.second_name}: {student_db_id}")

# 2. Создайте несколько книг и укажите, что ваш созданный студент взял их
books = ['The Silmarillion', 'The Hobbit']

# Словарь для хранения ID книг
book_db_ids = {}

# Создаем книги и сохраняем их ID
for book_title in books:
    book = Book(book_title, student_id=student_db_id)
    book_db_id = book.query_to_add_book()
    book_db_ids[book_title] = book_db_id
    print(f"ID добавленной книги '{book_title}': {book_db_id}")


# 3.Создайте группу (group) и определите своего студента туда:
student_group = Group('FC Barcelona', student_id=student_db_id)
group_db_id = student_group.add_group_and_assign_student()

print(f"ID добавленной группы {student_group.group_title}: {group_db_id}")

# 4.Создайте несколько учебных предметов (subjects)
# Создание списка, содержащего названия предметов
subjects = ['Питоноведение', 'Основы тестирования ПО']

# Словарь для хранения ID предметов
subject_db_ids = {}

# Создание предметов и сохранение их ID
for subject_name in subjects:
    subject = Subject(subject_name)
    subject_db_id = subject.query_to_add_subject()
    subject_db_ids[subject_name] = subject_db_id
    print(f"ID добавленного предмета '{subject_name}': {subject_db_id}")


# 5.Создайте по два занятия для каждого предмета (lessons):
lessons = {
    'Питоноведение': ['ч1', 'ч2'],
    'Основы тестирования ПО': ['ч1', 'ч2']
}

# Словарь для хранения ID занятий
lesson_db_ids = {}

# Создание занятий и сохранение их ID
for subject_name, lesson_parts in lessons.items():
    for part in lesson_parts:
        lesson = Lesson(f'{subject_name}, {part}', subject_id=subject_db_ids[subject_name])
        lesson_db_id = lesson.query_to_add_lesson()
        lesson_db_ids[f'{subject_name} {part}'] = lesson_db_id
        print(f"ID занятия {part} по предмету {subject_name}: {lesson_db_id}")

# 6. Проставление оценок студенту для всех созданных занятий
marks = ['High', 'Medium', 'Low', 'High']
mark_db_ids = {}

index = 0
for lesson_name, lesson_db_id in lesson_db_ids.items():
    mark = marks[index]
    mark_for_lesson = Mark(mark, lesson_id=lesson_db_id, student_id=student_db_id)
    mark_db_id = mark_for_lesson.query_to_add_mark_to_lesson()
    mark_db_ids[lesson_name] = mark_db_id
    print(f"ID оценки по занятию {lesson_name}: {mark_db_id}")
    index += 1


# Получение информации из базы данных
# 1.Все оценки студента:
cursor.execute('SELECT * FROM marks WHERE student_id = %s', (student_db_id,))
print(f"Информация о всех оценках студента: {cursor.fetchall()}")

# 2.Все книги, которые находятся у студента:
cursor.execute('SELECT * FROM books WHERE taken_by_student_id = %s', (student_db_id,))
print(f"Информация о всех книгах, которые взял студент: {cursor.fetchall()}")

# 3.Для вашего студента выведите всё, что о нем есть в базе:
# группа, книги, оценки с названиями занятий и предметов (всё одним запросом с использованием Join):
cursor.execute('SELECT * FROM students '
               'JOIN books '
               'ON students.id = books.taken_by_student_id '
               'JOIN `groups` '
               'ON students.group_id = groups.id '
               'JOIN marks ON students.id = marks.student_id '
               'JOIN lessons '
               'ON marks.lesson_id = lessons.id '
               'JOIN subjets '
               'ON lessons.subject_id = subjets.id '
               'WHERE students.id = %s', (student_db_id,))
print(f"Вся информация о созданном студенте: {cursor.fetchall()}")

db.commit()
db.close()
