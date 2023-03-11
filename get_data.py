import pandas as pd

# Load the dataset from url
url = 'https://gist.githubusercontent.com/curran/' \
      'a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/' \
      'iris.csv'

iris_dataframe = pd.read_csv(url)

# Remove edge-cases
iris_min = pd.DataFrame.min(iris_dataframe)
print(iris_min)

print(iris_dataframe.describe())
print(iris_dataframe.duplicated())

# sepal length vs sepal width (ratio)
# sepal length vs petal length
