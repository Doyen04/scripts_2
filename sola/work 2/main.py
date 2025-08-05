import pandas as pd

# Read the Excel file
df = pd.read_excel('./testfile.xlsx')

# Convert the date column to datetime and format it
# Replace 'DateColumn' with your actual column name
df['DATE OF BIRTH UPDATED'] = pd.to_datetime(df['DATE OF BIRTH UPDATED']).dt.strftime('%Y-%m-%d 00:00:00.000')

# Save back to Excel
with open('output.txt', 'w') as f:
    for _, row in df.iterrows():

        f.write(f"Update policymaster set DateofBirth='{row['DATE OF BIRTH UPDATED']}' where policyno='{row['Policy No']}' \n")



