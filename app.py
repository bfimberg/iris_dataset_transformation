import sqlite3
from io import StringIO
import csv
from flask import Flask, jsonify, make_response, render_template



app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    '''Function for getting all of the data from the database in a CSV format'''

    conn = sqlite3.connect('iris.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM iris_with_transformations')
    rows = cursor.fetchall()
    keys = [
        'sepal_length', 
        'sepal_width', 
        'petal_length', 
        'petal_width', 
        'species', 
        'sepal_ratio', 
        'length_ratio'
        ]

    data = [dict(zip(keys, row)) for row in rows]
    conn.close()
    return render_template(
        'data.html', 
        data=data)


@app.route('/average/<column_name>', methods=['GET'])
def get_average(column_name):
    '''Function for getting the average value of a column from database'''

    conn = sqlite3.connect('iris.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT {column_name} FROM iris_with_transformations')
    data = cursor.fetchone()[0]
    conn.close()
    return render_template('average.html', 
    data=data, 
    column_name=column_name)


@app.route('/range/<column_name>/<min_value>/<max_value>', methods=['GET'])
def get_range(column_name, min_value, max_value):
    '''Function for getting the value range of a column'''

    conn = sqlite3.connect('iris.db')
    cursor = conn.cursor()
    cursor.execute(
    f'SELECT {column_name} FROM iris_with_transformations WHERE {column_name} BETWEEN {min_value} AND {max_value}'
    )
    rows = cursor.fetchall()
    data = [row[0] for row in rows]

    conn.close()
    return render_template(
        'min_max.html',
         data=data, 
         column_name=column_name, 
         min_value=min_value, 
         max_value=max_value)


if __name__ == '__main__':
    app.run(debug=True)
