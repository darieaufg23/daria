# app.py

from flask import Flask, render_template, request, g
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)


# Маршрут для сторінки реєстрації
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                       (username, generate_password_hash(password)))
        print("hhh")
        db.commit()
        return f'Registration successful for {username}'

    return render_template('registration.html')

# Маршрут для сторінки входу
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()
        if user and check_password_hash(user[2], password):
            return f'You are logged in as {username}'
        else:
            return 'Incorrect username or password'

    return render_template('login.html')

# Маршрут для сторінки Dashboard
@app.route('/dashboard', methods= ['POST'])
def dashboard():
     
    username = request.form['fname']
    #password = request.form['password']
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                    (username, generate_password_hash("hjdsvcjd")))
    print("hhh")
    db.commit()
    
    cursor.execute("SELECT id, username FROM users")
    users = cursor.fetchall()
    print(users)
    
    return render_template('dashboard.html', users=users)

# Функції для роботи з базою даних
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('database.db', check_same_thread=False)
    return g.db

def initialize_db():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    db.commit()

if __name__ == '__main__':
    with app.app_context():
        initialize_db()
    app.run(debug=True)
