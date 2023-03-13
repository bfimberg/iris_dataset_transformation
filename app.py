import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route('/iris')
def get_iris_data():
    conn = sqlite3.connect('iris.db')
    cursor = conn.cursor()
    cursor.execute()