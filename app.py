from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='flask.cxayw68ko3pr.us-east-1.rds.amazonaws.com',
        user='admin',
        password='rajeshcentos',
        database='flask'
    )
    return connection

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        gender = request.form['gender']
        mobile_number = request.form['mobile_number']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO userdata (name, email, age, gender, mobile_number) 
            VALUES (%s, %s, %s, %s, %s)
        ''', (name, email, age, gender, mobile_number))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('success'))

    return render_template('form.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
