import sqlite3

conn = sqlite3.connect("database.db")

print("Opened database successfully")

conn.execute("Create table Emp(FName TEXT, LName TEXT, AddL1 TEXT, AddL2 TEXT,Pin TEXT, IsActive TEXT)")

print("table created successfully")

conn.close()