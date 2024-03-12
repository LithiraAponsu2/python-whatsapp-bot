import csv
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='1234',
    database='mydb'
)
cursor = conn.cursor()

# Read the first row of the CSV file to get column names
with open('products.csv', 'r') as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)

# Generate SQL CREATE TABLE statement dynamically
create_table_sql = f"CREATE TABLE IF NOT EXISTS my_table ({', '.join([f'{header} VARCHAR(255)' for header in headers])})"
cursor.execute(create_table_sql)

# Read data from CSV and insert into the database
with open('products.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header if it exists
    for row in csv_reader:
        cursor.execute(f"INSERT INTO my_table ({', '.join(headers)}) VALUES ({', '.join(['%s'] * len(row))})", row)

# Commit changes and close connection
conn.commit()
conn.close()
