from flask import Flask, render_template, request

import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def back():
    return render_template('back.html')


@app.route('/EnterNew')
def new_employee():
    return render_template('employee.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            fnm = request.form['fnm']
            lnm = request.form['lnm']
            add1 = request.form['add1']
            add2 = request.form['add2']
            pin = request.form['pin']
            Isactive = request.form['Isactive']

            with sql.connect("database.db") as con:

                cur = con.cursor()

                cur.execute("INSERT INTO Emp(FName,LName,AddL1,AddL2,Pin,IsActive) VALUES (?,?,?,?,?,?)")

                msg = "Record Successfully Added"

        except:
            con.rollback()
            msg = "error in insert operation"
            con.close()

        finally:
            return render_template("result.html", msg=msg)


@app.route('/List')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("select * from Emp")

    rows = cur.fetchall()

    return render_template("list.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
