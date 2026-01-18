import sqlite3
import os
import sys


# Connect to database in SalesDB folder
db_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'SalesDB', 'sales.db')
conn = sqlite3.connect(db_path)

cursor = conn.cursor()
cursor.execute("""Select * from orders""")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
print(f"Database accessed successfully at: {db_path}")