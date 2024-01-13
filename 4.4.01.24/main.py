from src.app import app
import sqlite3

conn = sqlite3.connect("user_data.db")
app.run()