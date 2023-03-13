import sqlite3
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/iris', methods=['GET'])
def get_data():
    '''Function for getting all of the data from the database'''

    conn = sqlite3.connect('iris.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM iris_with_transformations')
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)


@app.route('/average/<column_name>', methods=['GET'])
def get_average(column_name):
    '''Function for getting the average value of a column from database'''

    conn = sqlite3.connect('iris.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT {column_name} FROM iris_with_transformations')
    average = cursor.fetchone()[0]
    conn.close()
    return jsonify(average)


@app.route('/range/<column_name>/<min_value>/<max_value>', methods=['GET'])
def get_range(column_name, min_value, max_value):
    '''Function for getting the value range of a column'''

    conn = sqlite3.connect('iris.db')
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM iris_with_transformations WHERE {column_name} BETWEEN {min_value} AND {max_value}')
    rows = cur.fetchall()
    conn.close()
    return jsonify(rows)


if __name__ == '__main__':
    app.run(debug=True)
