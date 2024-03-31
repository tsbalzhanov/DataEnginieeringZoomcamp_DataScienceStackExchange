import pandas as pd


def add_month_column(df: pd.DataFrame, date_column: str, month_column: str) -> pd.DataFrame:
    df[month_column] = df[date_column].apply(lambda date: date.strftime('%Y-%m')).astype(pd.StringDtype())
    return df


def add_post_partition_column(df: pd.DataFrame, post_id_column: str, partition_id_column: str, **kwargs) -> pd.DataFrame:
    df[partition_id_column] = df[post_id_column] % kwargs['POST_ID_PARTITIONS_NUM']
    return df
