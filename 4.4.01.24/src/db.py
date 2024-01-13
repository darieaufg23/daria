import sqlite3

def create_conn():
    return sqlite3.connect(db_name)

def insert_data_row(cr, name, surname, email, date, phone):
    
conn = create_conn("user_data.db")