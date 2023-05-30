import sqlite3

# Connect to the SQLite
conn = sqlite3.connect('employeelist.db')
cursor = conn.cursor()

# Employee table
create_table_query = '''
CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    designation TEXT,
    salary INTEGER
)
'''
cursor.execute(create_table_query)

# Table Created
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='employee'")
table_exists = cursor.fetchone()
if table_exists:
    print("Employee table created successfully.")

# Insert data
insert_data_query = '''
INSERT INTO employee (name, designation, salary)
VALUES (?, ?, ?)
'''
employees = [
    ("Amimul", "Analyist", 25000),
    ("Fahim", "Developer", 35000)
]
cursor.executemany(insert_data_query, employees)
conn.commit()
print("Employee data inserted successfully.")

# Display all employee data
select_data_query = "SELECT * FROM employee"
cursor.execute(select_data_query)
rows = cursor.fetchall()

print("\nEmployee data:")
print(rows)

# Close the database connection
conn.close()