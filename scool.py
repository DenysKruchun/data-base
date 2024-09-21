import sqlite3

connection =  sqlite3.connect("school.db")
cursor = connection.cursor()
cursor.execute(''' SELECT * FROM students''')
students = cursor.fetchall()
print(students)
connection.close()

# ДОМАШНЄ ЗАВДАННЯ 

# 1) Отримання і вивід всіх учнів   7 класу з БД
# 2) Вивести список всіх вчителів
# 3) Додати в БД 2 нових учнів 5 класу
# 4) Вивести список оцінок усіх учнів
# 5) Вивести список усіх відмінних оцінок (10 і вище)
# 6) Вивести список оцінок усіх учнів 5 класу

