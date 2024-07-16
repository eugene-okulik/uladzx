students = ['Ivanov', 'Petrov', 'Sidorov']

subjects = ['math', 'biology', 'geography']


# result text should be: Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geography

result = f'Students {students[0]}, {students[1]}, {students[2]} study these subjects: \
{subjects[0]}, {subjects[1]}, {subjects[2]}'

print(result)
