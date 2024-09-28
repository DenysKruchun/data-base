import sqlite3

class DatabaseManager ():
    def __init__(self):
        self.connection  = sqlite3.connect("shop.db")
        self.cursor = self.connection.cursor()

    def get_all_items(self):
        self.cursor.execute('''SELECT * FROM items ''')
        items = self.cursor.fetchall()
        return items
     
     

    
        