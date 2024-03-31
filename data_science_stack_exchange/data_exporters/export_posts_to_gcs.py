from pandas import DataFrame

from data_science_stack_exchange.utils.helpers.exporters import upload_partitioned_table_to_gcs


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    table_name = 'posts'
    gcs_paths = upload_partitioned_table_to_gcs(df, table_name, ['CreationMonth'], **kwargs)
    return {table_name: gcs_paths}
