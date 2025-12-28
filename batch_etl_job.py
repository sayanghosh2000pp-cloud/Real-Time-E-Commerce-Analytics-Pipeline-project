import pandas as pd
df = pd.read_csv('data/raw/transactions.csv')
df_grouped = df.groupby('category')['amount'].sum().reset_index()
df_grouped.to_csv('data/processed/aggregated_sales.csv', index=False)
