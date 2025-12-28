import pandas as pd

def validate_data(df):
    df = df.drop_duplicates()
    df = df.dropna(subset=["order_id", "user_id", "amount", "category"])
    df = df[df["amount"] > 0]
    return df
