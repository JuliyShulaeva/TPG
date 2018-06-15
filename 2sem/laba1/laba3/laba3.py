import sys
import sqlite3
import csv


conn = sqlite3.connect(":memory:")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()  # взаимодействие с базой
kol = 0

# Создание таблицы
tb_create = cursor.execute("""CREATE TABLE student
               (id int, first_name char, middle_name char, last_name char, group_name char, faculty char, age int)""")

with open('spisok.csv', newline='') as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        # Вставляем данные в таблицу
        cursor.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?, ?, ?)", row)
        print('row = ', row)

#reader = csv.reader(sys.stdin, delimiter=";")
#for row in reader:
    #Вставляем данные в таблицу
    #cursor.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?, ?, ?)", row)
    #print('row = ', row)

conn.commit()

cursor.execute("SELECT COUNT(id) FROM student WHERE age > 81 AND faculty = 'FCS' AND last_name like 's%'")
number = cursor.fetchall()
print(format(number[0][0]))

conn.close()
