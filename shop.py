from database import DatabaseManager

db = DatabaseManager()

while True:
    print("1- Переглянути всі товари \n2 - Додати до кошика \n0- Вихід")
    action = input("Виберіть дію: ")
    if action == "0":
        break
    elif action == "1":
        items = db.get_all_items()
        for item in items:
            print(f"{item[0]} - {item[1]} - {item[2]} гривень!")
    
     
    # ДЗ
    #  додати дії: 
    #  виведення списку категорій
    #  виведення товарів з певної категорії
    #  детальний перегляд інформації про товар за ID товару
    #  пошук товару по назві 

