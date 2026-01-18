import sqlite3
import os
import sys

# Create SalesDB folder if it doesn't exist
db_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'SalesDB')
os.makedirs(db_folder, exist_ok=True)

# Connect to database in SalesDB folder
db_path = os.path.join(db_folder, 'sales.db')
conn = sqlite3.connect(db_path)
# cursor = conn.cursor()
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_name TEXT,
    quantity INTEGER,
    price REAL,
    total REAL
)""")

cursor.execute("""INSERT INTO orders (customer_id, product_name, quantity, price, total) VALUES
(1, 'Laptop', 1, 1000.00, 1000.00),
(2, 'Smartphone', 2, 500.00, 1000.00),
(3, 'Tablet', 1, 300.00, 300.00),   
(4, 'Headphones', 3, 100.00, 300.00),
(5, 'Smartwatch', 1, 200.00, 200.00)
""")

conn.commit()
conn.close()
print(f"Database created successfully at: {db_path}")