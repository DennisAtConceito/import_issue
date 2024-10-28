import pandas as pd
#Python 3.12.7
#pandas 2.2.2
#openpyxl 3.1.5

df = pd.read_excel('2_rows_to_skip.xlsx', skiprows=[0,1], header=[0,1])
df2 = pd.read_excel('1_row_to_skip.xlsx', skiprows=[0], header=[0,1])

#print(df)

for col in df.columns:
    print(col)
    
print('-------------------')

for col in df2.columns:
    print(col)
