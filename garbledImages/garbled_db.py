# import hashlib
# import sqlite3
# import os


# conn = sqlite3.connect("garbled_db.db")
# cursor = conn.cursor()

# print('Database created')

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS garbled_table (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         filename TEXT,
#         original_text TEXT
#     )
# ''')

# conn.commit()
# print('Table Created')

# def insert_data(filename, original_text):
#     cursor.execute('SELECT * FROM garbled_table WHERE filename = ? AND original_text = ?', (filename, original_text))
#     existing_data = cursor.fetchone()
#     # If data does not exist, insert it
#     if not existing_data:
#         # Insert data into the table
#         cursor.execute('INSERT INTO garbled_table (filename, original_text) VALUES (?, ?)', (filename, original_text))
#         conn.commit()
    
# image_folder = '.'

# # Iterate through each file in the folder
# for filename in os.listdir(image_folder):
#     if filename.endswith(".jpg") or filename.endswith(".png"):  # Adjust file extensions as needed
#         # You may want to extract original_text from the file or provide a default value
#         base_name, extension = os.path.splitext(filename)
#         original_text = base_name
#         h = hashlib.new('sha512_256') 
#         h.update(base_name.encode())
#         original_text = h.hexdigest()
#         # Insert data into the authentication_info table
#         insert_data(filename, original_text)

# print('Data filled successfully...')   
# conn.commit()
# conn.close()


import hashlib
import sqlite3
import os

def create_database():
    conn = sqlite3.connect("garbled_db.db")
    cursor = conn.cursor()

    print('Database created')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS garbled_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            original_text TEXT
        )
    ''')

    conn.commit()
    print('Table Created')
    conn.close()

def insert_data(filename, original_text):
    conn = sqlite3.connect("garbled_db.db")
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM garbled_table WHERE filename = ? AND original_text = ?', (filename, original_text))
    existing_data = cursor.fetchone()
    # If data does not exist, insert it
    if not existing_data:
        # Insert data into the table
        cursor.execute('INSERT INTO garbled_table (filename, original_text) VALUES (?, ?)', (filename, original_text))
        conn.commit()
    
    conn.close()

def main():
    create_database()

    image_folder = 'garbledImages'

    # Iterate through each file in the folder
    for filename in os.listdir(image_folder):
        if filename.endswith((".jpg", ".png", ".jpeg", ".gif")):  # Adjust file extensions as needed
            # You may want to extract original_text from the file or provide a default value
            base_name, extension = os.path.splitext(filename)
            original_text = base_name
            h = hashlib.new('sha512_256') 
            h.update(base_name.encode())
            original_text = h.hexdigest()
            # Insert data into the authentication_info table
            insert_data(filename, original_text)

    print('Data filled successfully...')

if __name__ == "__main__":
    main()
