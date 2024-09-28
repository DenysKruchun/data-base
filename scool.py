import sqlite3

connection =  sqlite3.connect("school.db")
cursor = connection.cursor()
cursor.execute(''' SELECT * FROM students''')
students = cursor.fetchall()


cursor.execute('''DELETE  FROM students WHERE name = "Serhii" ''')
cursor.execute('''DELETE  FROM students WHERE name = "yef" ''')
bad_students = cursor.fetchall()
connection.commit()

# cursor.execute('''INSERT INTO students("name","surname","grade","age")
#                VALUES (?,?,?,?)''',["Anna","Kravets",8,16])
# connection.commit()



cursor.execute('''UPDATE students
               SET age = 15
               WHERE id = 75''')
connection.commit()


cursor.execute('''SELECT s.title, s.grade, t.name, t.surname
               FROM teachers t
               INNER JOIN subjects s  ON s.id = t.subject_id
               WHERE s.title = "math"  ''')

teachers = cursor.fetchall()
for teacher in teachers:
    print(f"{teacher[2]} {teacher[3]} teaches  {teacher[0]} at {teacher[1]} grade !!!")


# ДОМАШНЄ ЗАВДАННЯ 

# # 1) Отримання і вивід всіх учнів   7 класу з БД
# cursor.execute('''SELECT * FROM students WHERE grade = 8''')
# students = cursor.fetchall()
# for student in students:
#     print(student[1],student[2])

# # 2) Вивести список всіх вчителів
# cursor.execute('''SELECT * FROM teachers''')
# teachers = cursor.fetchall()
# for student in teachers:
#     print(student[1],student[2])

# # 3) Додати в БД 2 нових учнів 5 класу
# # cursor.execute('''INSERT INTO students ("name","surname",grade,age)
# #                VALUES(?,?,?,?)''',["Serhii","Sadov",5,10])

# # cursor.execute('''INSERT INTO students ("name","surname",grade,age)
# #                VALUES(?,?,?,?)''',["yef","tytff",5,10])

# # connection.commit()
# print("______________")
# # 4) Вивести список оцінок усіх учнів
# cursor.execute('''SELECT marks.point, marks.created, students.name, students.surname , students.grade 
#                FROM marks 
#                INNER JOIN students ON marks.student_id = students.id''')
# marks = cursor.fetchall()

# for mark in marks:
#     print(mark[0] ,"-" ,mark[2],mark[3] )
# print("______________")
# # 5) Вивести список усіх відмінних оцінок (10 і вище)
# cursor.execute('''SELECT m.point, sub.title, s.name, s.surname , s.grade,  m.created
#                FROM marks m
#                INNER JOIN students s ON m.student_id = s.id
#                INNER JOIN subjects sub ON m.subject_id = sub.id 
#                WHERE m.point >= 10
#                ''')
# marks = cursor.fetchall()
# for mark in marks:
#     print(mark[0] ,"-" ,mark[1] ,"-", mark[2],mark[3] )
# # 6) Вивести список оцінок усіх учнів 5 класу
# print("______________")
# cursor.execute('''SELECT m.point, m.created, s.name, s.surname , s.grade 
#                FROM students s
#                LEFT OUTER JOIN marks m ON s.id = m.student_id ''')
# marks = cursor.fetchall()

# for mark in marks:
#     print(mark[0] ,"-" ,mark[2],mark[3], "-" , mark[4], "class" )

# print("______________")
# cursor.execute('''SELECT t.surname, t.name , s.title, s.grade
#                FROM teachers t
#                 INNER JOIN subjects s ON t.subject_id = s.id    
#                WHERE s.grade = 5''')
# teachers = cursor.fetchall()
# for teacher in teachers:
#     print(f"{teacher[0]  }  {teacher[1]} - {teacher[2]} grade:{teacher[3]}")
connection.close()

