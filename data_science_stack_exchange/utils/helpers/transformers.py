import pandas as pd


def add_month_column(df: pd.DataFrame, date_column: str, month_column: str) -> pd.DataFrame:
    df[month_column] = df[date_column].apply(lambda date: date.strftime('%Y-%m')).astype(pd.StringDtype())
    return df


def _add_partition_column(df: pd.DataFrame, id_column: str, partition_id_column: str, n_partitions: int) -> None:
    df[partition_id_column] = df[id_column] % n_partitions


def add_post_partition_column(df: pd.DataFrame, post_id_column: str, **kwargs) -> pd.DataFrame:
    _add_partition_column(df, post_id_column, kwargs['POST_ID_PARTITIONS_COLUMN'], kwargs['POST_ID_PARTITIONS_NUM'])
    return df


def add_user_partition_column(df: pd.DataFrame, user_id_column: str, **kwargs) -> pd.DataFrame:
    _add_partition_column(df, user_id_column, kwargs['USER_ID_PARTITIONS_COLUMN'], kwargs['USER_ID_PARTITIONS_NUM'])
    return df
