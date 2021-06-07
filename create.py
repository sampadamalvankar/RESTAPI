import sqlite3
import sqlite3 as sql

from app import app


def main():
    try:
        conn = sqlite3.connect("database.db")

        cur = con.cursor()

        table = "CREATE TABLE Emp (FName,LName,AddL1,AddL2,Pin,IsActive)"

        cur.execute(table)
        print("Table created")

    except sql.Error as e:
        print("Unable to create table")


if __name__ == '__main__':
    app.run(debug=True)


