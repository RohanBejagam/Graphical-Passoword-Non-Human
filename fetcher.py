import os
import hashlib
import sqlite3

def fetcher(filename):
    base_name, extension = os.path.splitext(filename)
    h = hashlib.new('sha512_256')
    h.update(base_name.encode())
    base_name = h.hexdigest()
    conn = sqlite3.connect('./garbledImages/garbled_db.db')
    cursor = conn.cursor()

    cursor.execute('SELECT original_text from garbled_table WHERE original_text=?', [base_name, ])
    return cursor.fetchone()[0]