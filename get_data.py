import sqlite3
import pandas as pd

# Load the dataset from url
URL = 'https://gist.githubusercontent.com/curran/' \
      'a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/' \
      'iris.csv'

# Create dataframe
iris_dataframe = pd.read_csv(URL)

# Remove edge-cases (2 standard deviations away from mean)
iris_numeric = iris_dataframe.select_dtypes(exclude=['object'])
iris_numeric_mean = iris_numeric.mean()
iris_numeric_std_dev = iris_numeric.std()
iris_numeric = iris_numeric[
      (iris_numeric - iris_numeric_mean).abs() <= 2 * iris_numeric_std_dev
      ].dropna()
iris_dataframe.update(iris_numeric)

# Create new columns: ratio of sepal length and sepal width,  ratio of sepal length and petal length
iris_dataframe['sepal_ratio'] = iris_dataframe['sepal_length'] / iris_dataframe['sepal_width']
iris_dataframe['length_ratio'] = iris_dataframe['sepal_length'] / iris_dataframe['petal_length']
iris_dataframe['sepal_ratio'] = iris_dataframe['sepal_ratio'].astype(float).round(2)
iris_dataframe['length_ratio'] = iris_dataframe['length_ratio'].astype(float).round(2)

# Store the dataframe in a CSV file
iris_dataframe.to_csv('iris_with_transformations', index=False)

# Connect to the SQLite database
conn = sqlite3.connect('iris.db')

# Write the gathered and transformed data to the database
iris_dataframe.to_sql('iris_with_transformations', conn, if_exists='replace', index=False)

conn.close()
