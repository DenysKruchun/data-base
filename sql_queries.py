import sqlite3

connection =  sqlite3.connect("Artists.db")
cursor = connection.cursor()


# Запитання 1. Інформація про скількох художників представлена у базі даних?
# cursor.execute("SELECT  * FROM artists")
# artist = cursor.fetchall()
# print(len(artist))

# Запитання 2. Скільки жінок (Female) у базі?
# cursor.execute('''SELECT  * FROM artists WHERE "Gender" = "Female" ''')
# women = cursor.fetchall()
# print(len(women))


# Запитання 3. Скільки людей у базі даних народилися до 1900 року?
# cursor.execute('''SELECT  * FROM artists WHERE "Birth Year" < 1900 ''')
# birth = cursor.fetchall()
# print(len(birth))


# Запитання 4. Додати в базу даних ще двох художників
# cursor.execute('''INSERT INTO artists("Artist ID","Name","Nationality","Gender","Birth Year")
#                VALUES(?,?,?,?,?) ''',[579,"Picasso","Spanish","Male",1881])
# connection.commit()

# cursor.execute('''INSERT INTO artists("Artist ID","Name","Nationality","Gender","Birth Year")
#                VALUES(?,?,?,?,?) ''',[580,"Da Vinci","Italian","Male",1452])
# connection.commit()



# Запитання 5. Надрукувати список усіх художників з Швеції (Swedish)
# cursor.execute('''SELECT  * FROM artists WHERE "Nationality" = "Swedish" ''')
# sweeden  = cursor.fetchall()
# for artist in sweeden:
#     print(f'{artist[1]} - {artist[-1]}')





# ДОМАШНЄ ЗАВДАННЯ 
# Скільки художників в базі даних мають національність "American"?
cursor.execute('''SELECT * FROM artists WHERE "Nationality" = "American" ''')
american = cursor.fetchall()
# for artist in american:
print(len(american))


# Додаткове завдання* Як звати  наймолодшого художника?

# Знайти художника з найстарішим роком народження (тобто найстаршого художника).


cursor.execute('''SELECT * FROM artists ORDER BY "Birth Year" DESC''')
artist = cursor.fetchone()

print (f"{artist[1]} - {artist[-1]}")



# Знайти всіх художників, які народилися між 1850 і 1900 роками.


# cursor.execute(''' SELECT * FROM artists WHERE "Birth Year" >= 1850 AND "Birth Year"  <= 1900''')
# years = cursor.fetchall()
# for artist in years:
#     print(f"{artist[-1]} - {artist[1]}")


# Видалити художника з бази даних з ідентифікатором 422.


# cursor.execute(''' DELETE  FROM artists WHERE "Artist Id" = 422''')
# id = cursor.fetchall()
# connection.commit()


connection.close()














