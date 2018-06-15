import sqlite3
import csv


class Student(object):
    def __init__(self, data, curs):
        for key, value in data.items():
            object.__setattr__(self, key, value)
        object.__setattr__(self, 'cursor', curs)

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)
        request_from_the_table = 'UPDATE student SET {} = ? WHERE id = ?'.format(key)
        # UPDATE - производит изменения; SET - вставки нового значения; WHERE - ограничение выбранного охвата
        self.cursor.execute(request_from_the_table, (value, self.id))


def find(id_1, cursor):
    cursor.execute("SELECT * FROM student WHERE id = ?", [int(id_1)])
    # SELECT * FROM - запрос из таблицы; WHERE - ограничение выбранного охвата
    obj = {}
    for des, value in zip(cursor.description, cursor.fetchone()):
        # desc перебирает по cursor.description, это заголовки таблицы;
        # value перебирает по cursor.fetchone, в нем лежат все поля из найденного студента
        obj[des[0]] = value
    return obj


conn = sqlite3.connect('data_base.sqlite')  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()  # взаимодействие с базой
# Создание таблицы
cursor.execute("""CREATE TABLE student
               (id int, first_name char, middle_name char, last_name char, group_name char, faculty char, age int)""")

with open('spisok.csv', newline='') as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        # Вставляем данные в таблицу
        cursor.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?, ?, ?)", row)
        print('row = ', row)
    conn.commit()

work = find(1, cursor)
stud = Student(work, cursor)
stud.first_name = 'ROMAN'


conn.commit()
conn.close()
