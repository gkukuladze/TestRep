import pandas as pd

file_path = '/mnt/data/titanic.csv'
titanic_data = pd.read_csv(file_path)

survived_data = titanic_data[titanic_data['Survived'] == 1]

output_file_path = '/mnt/data/survived.csv'
survived_data.to_csv(output_file_path, index=False)

output_file_path
