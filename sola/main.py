import pandas as pd

# Replace 'your_file.xlsx' with your Excel file name
df = pd.read_excel('./testfile.xlsx')

# Replace 'ColumnName' with the name of the column you want to read
column_data = df['Policy No']

print(column_data)
with open('output.txt', 'w') as f:
    for item in column_data:
        f.write(f"'{item}',")