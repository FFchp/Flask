from flask import Flask, render_template
from flask.helpers import url_for
import pymysql.cursors
from werkzeug.utils import redirect
from werkzeug.wrappers import request

app = Flask(__name__)
conn = pymysql.connect( host = 'localhost',
                        user = 'root',
                        password = '',
                        database = 'studentdb')

@app.route("/")
def show():
    with conn:
        cur = conn.cursor()
        cur.execute("select * from student")
        row = cur.fetchall()
        return render_template('index.html', data = row)

@app.route("/addinfo")
def add():
        return render_template('add.html')

@app.route("/insert", method=['POST'])
def insert():
    if request.method=="POST":
        fname = request.form['fname']
        lname = request.form['lname']
        with conn.cursor() as cursor:
            sql="insert into 'student' ('fname', 'lname') values(%s,%s)"
            cursor.execute(sql,(fname, lname))
            conn.commit()
        return redirect(url_for('showData'))

if __name__ == "__main__":
    app.run(debug=True)

