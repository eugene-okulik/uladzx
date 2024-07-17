students = ['Ivanov', 'Petrov', 'Sidorov']

subjects = ['math', 'biology', 'geography']


# result text should be: Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geography

print('Students', ', '.join(students) + ' study these subjects:', ', '.join(subjects))
