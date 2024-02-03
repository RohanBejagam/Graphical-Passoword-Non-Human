import hashlib
import sqlite3
import os


conn = sqlite3.connect("obscure_db.db")
cursor = conn.cursor()

print('Database created')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS obscured_table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        original_obscured TEXT
    )
''')

conn.commit()
print('Table Created')

def insert_data(filename, original_obscured):
    # Insert data into the table
    cursor.execute('INSERT INTO obscured_table (filename, original_obscured) VALUES (?, ?)', (filename, original_obscured))
    
image_folder = '.'

filepath = "original_obscure.txt"

f = open(filepath, "r")
for line in f:
    # line = f.readline()
    data= line.split(' ')
    filename=data[0]
    text=data[1:]
    obscured_text_temp = '-'.join(text)
    obscured_text_temp = obscured_text_temp[:-1]
    # print(obscured_text_temp+" next like ki poindi")
    
    insert_data(filename,obscured_text_temp)
    


print('Data filled successfully...')   
conn.commit()
conn.close()