import pandas as pd

from data_science_stack_exchange.utils.helpers.exporters import upload_partitioned_table_to_gcs

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_google_cloud_storage(df: pd.DataFrame, **kwargs) -> None:
    table_name = 'votes'
    gcs_paths = upload_partitioned_table_to_gcs(df, table_name, **kwargs)
    return {**gcs_paths, 'table_name': table_name}
