import pandas as pd
import numpy as np

# Seed set kiya hai taaki har baar same data bane
np.random.seed(42)
n_rows = 150

# Custom E-commerce Customer Dataset
data = {
    'Customer_ID': [f'CUST_{1000 + i}' if i % 12 != 0 else np.nan for i in range(n_rows)],
    'Join_Date': pd.date_range(start='2023-01-01', periods=n_rows, freq='2D'),
    'Age': [np.random.randint(18, 65) if i % 7 != 0 else np.nan for i in range(n_rows)],
    'Gender': np.random.choice(['Male', 'Female', 'Other'], size=n_rows, p=[0.48, 0.48, 0.04]),
    'City': np.random.choice(['Karachi', 'Lahore', 'Islamabad', 'Peshawar'], size=n_rows),
    'Category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Books'], size=n_rows),
    'Order_Count': np.random.randint(1, 30, size=n_rows),
    'Total_Spent': [round(np.random.uniform(500, 50000), 2) if i % 9 != 0 else np.nan for i in range(n_rows)],
    'Is_VIP': np.random.choice([True, False], size=n_rows, p=[0.2, 0.8])
}

df = pd.DataFrame(data)
print("Dataset Ready! Total rows:", len(df))
df.head()



# 1

print(f"shape: {df.shape}")
print(f"\ndata types: \n{df.dtypes}")
print(f"\nMissing values in each column: \n{df.isnull().sum()}")



# 2

df = df.dropna(subset=['Customer_ID'])
print(f"after drop: {df.shape}")



# 3

df['Age'] = df['Age'].fillna(df['Age'].median())
df['Total_Spent'] = df['Total_Spent'].fillna(df['Total_Spent'].mean())



# 4

df['Join_Date'] = pd.to_datetime(df['Join_Date'])
df['Join_Year'] = df['Join_Date'].dt.year
df['Join_Month'] = df['Join_Date'].dt.month_name()


# 5

df['Avg_Order_Value'] = df['Total_Spent'] / df['Order_Count']


# 6

df['High_Value_Customer'] = df['Avg_Order_Value'] > 2500


# 7


print(f"total customers per city:\n{df.groupby('City')['Customer_ID'].count()}")
print(f"\navg total spent per city:\n{df.groupby('City')['Total_Spent'].mean()}")
print(f"\nmax  order count per city:\n{df.groupby('City')['Order_Count'].max()}")


# 8

table = pd.pivot_table(df, index='Category', columns='Is_VIP', values='Total_Spent', aggfunc='sum')
print(f"\n{table}")


# 9 

temp = df[df['Category'].isin(['Electronics', 'Clothing'])]
top = temp.nlargest(5, 'Total_Spent')

print(f"\n{top}")


# 10

kvip = df[(df['City'] == 'Karachi') & (df['Is_VIP'] == True)]
lvip = df[(df['City'] == 'Lahore') & (df['Is_VIP'] == True)]

print(f"\nkarachi vip avg count: {kvip['Order_Count'].mean()}")
print(f"lahore vip avg count: {lvip['Order_Count'].mean()}")