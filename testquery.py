import pandas as pd


csv_file_path = 'contact_data.csv'
target_keyword = 'Waters'

df = pd.read_csv(csv_file_path)

# Specify the columns you want to search in
columns_to_search = ['First', 'Last', 'Phone', 'Email']

# Perform the search
result = df[df[columns_to_search].apply(lambda row: target_keyword in row.values, axis=1)]

print(result)
