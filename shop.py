from database import DatabaseManager

db = DatabaseManager()
current_order = None

while True:
    print("__________________________________")
    print("1- Переглянути всі товари \n2 - Категорії\n 3- Оформити замовлення \n0- Вихід")
    action = input("Виберіть дію: ")
    if action == "0":
        break
    elif action == "1":
        print("Товари:")
        items = db.get_all_items()
        for item in items:
            print(f"{item[0]} - {item[1]} - {item[3]} гривень!")

        item_id = input("ВВедіть ід товару:")
        item = db.get_item(item_id)
        print(f"----------------------------")
        print(f"{item[4]}\n{item[1]} \n{item[2]}\n{item[3]}  гривень!")
        answer  = input("Чи ви хочете додати  товар до кошика?").lower()
        if answer == "так":
            if not current_order:
                current_order = db.create_order()
            quantity = int(input("Скільки одиниць товару бажаєте придбати?"))
            db.add_item_in_order(item_id,current_order,quantity )
            print("Товар додано до кошика!")





    elif action == "2":
        print("Категорії:")
        categories = db.get_all_categories()
        for category in categories:
            print(f"{category[0]} - {category[1]}")
        category_id = int(input("ВВедіть айді категорії:"))
        items = db.get_items_by_category_id(category_id)
        for item in items:
            print(f"{item[0]} - {item[1]} - {item[3]} гривень!")


    elif action == "3":
        if current_order:

            full_name = input("Введіть ПІБ:")
            phone_number  = input("Введіть номер  телефону:")
            address = input("Введіть адресу:")
            payment_type = input("ВВедіть тип платежу:")
            city = input("Введіть ваше місто:")
            db.update_order(full_name,phone_number,address,payment_type,city,current_order)
            print("Замовлення оформлено!!!")
            current_order = None


    # ДЗ
    #  додати дії:
    #  виведення списку категорій
    #  виведення товарів з певної категорії
    #  детальний перегляд інформації про товар за ID товару
    #  пошук товару по назві
