import pandas as pd

# Read Excel file
df = pd.read_excel('./test.xlsx')

# Read all data in the 'Policy No' column
column_data = df['RefNumber']

# Write the column data to a text file
df_uniq = df.drop_duplicates(subset='RefNumber', keep='first')

df_uniq.to_excel('unique_refnumber.xlsx', index=False)
print(df_uniq.head())
#VoucherNo
column_data = df_uniq['VoucherNo']
with open('output.txt', 'w') as f:
    for item in column_data:
        f.write(f"'{item}',")
print("Column data written to output.txt")