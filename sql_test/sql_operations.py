import sqlite3
import os.path

def update_row(cursor, con):
    print('------------------PRINT ALL---------------------')
    integer = int(input('Enter id: '))
    name = str(input('Enter name: '))
    email = str(input('Enter email: '))
    
    sql_update_query = f'''UPDATE user SET name='{name}', email='{email}' WHERE id = {integer} '''
    cursor.execute(sql_update_query)
    con.commit()
    
def delete_row(cursor, con):
    print('------------------PRINT ALL---------------------')
    integer = int(input('Enter id: '))
    sql_delete_query = f"""DELETE from user where id = {integer}"""
    cursor.execute(sql_delete_query)
    con.commit()    

def print_all(cursor):
    print('------------------PRINT ALL---------------------')
    cursor.execute("SELECT * FROM user")

    rows = cursor.fetchall()

    for row in rows:
        print(row)    
        
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")

con = sqlite3.connect(db_path)
cursor = con.cursor()

name = str(input('Enter name: '))
email = str(input('Enter email: '))

cursor.execute(f"INSERT INTO user (name, email) VALUES ('{name}', '{email}')")
con.commit()
print_all(cursor)
delete_row(cursor, con)
print_all(cursor)
update_row(cursor, con)
print_all(cursor)

con.close()