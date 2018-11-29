import pymysql
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def base():
    return "Ziyu Zhang HW12. \n" + "Enter */ins_table to acess table."


@app.route('/ins_table')
def ins_summary():
    pwd = input("Enter root password.")
    db = pymysql.connect("localhost", "root", str(pwd), "sswrepository_zzy")
    cursor = db.cursor()
    query = """select CWID, Name, Dept, course, stuNum from instructors_re;"""
    cursor.execute(query)
    rows = cursor.fetchall()
    data = [{'cwid': cwid, 'name': name, 'dept': dept, 'course': course, 'stuNum': stuNum} for cwid, name, dept, course, stuNum in rows]

    return render_template('ins_table.html', my_header='Stevens Repository by ZZY', table_title='Instructors Summary', ins=data)


app.run(debug=True)
