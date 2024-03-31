import pathlib

import pandas as pd


def load_and_parse_dataframe(file_path: pathlib.Path | str, dtypes: dict, date_fields: list[str]) -> pd.DataFrame:
    df = pd.read_xml(file_path, dtype=dtypes)
    for date_field in date_fields:
        df[date_field] = pd.to_datetime(df[date_field], errors='coerce', format='ISO8601')
    return df
