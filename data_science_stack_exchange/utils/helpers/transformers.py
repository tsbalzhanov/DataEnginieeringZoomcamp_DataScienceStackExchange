import pandas as pd


def add_month_column(df: pd.DataFrame, date_column: str, month_column: str) -> pd.DataFrame:
    df[month_column] = df[date_column].apply(lambda date: date.strftime('%Y-%m')).astype(pd.StringDtype())
    return df
