import pandas as pd 
import os

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, 27, 22, 32],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
        }

df = pd.DataFrame(data)

#adding new row to the dataframe
new_row = {'Name': 'Eve', 'Age': 29, 'City': 'San Francisco'}
df.loc[len(df.index)] = new_row

#adding new row to the dataframe
new_row2 = {'Name': 'Frank', 'Age': 35, 'City': 'Seattle'}
df.loc[len(df.index)] = new_row2


data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'simple_data.csv')

df.to_csv(file_path, index=False)

print(f"DataFrame saved to {file_path}")