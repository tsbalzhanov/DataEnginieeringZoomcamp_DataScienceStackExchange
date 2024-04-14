import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from .google_cloud import setup_google_cloud_credentials


def upload_partitioned_table_to_gcs(df: pd.DataFrame, table_path_postfix: str, **kwargs) -> list[str]:
    partition_cols = []
    for key in ('POST_ID_PARTITIONS_COLUMN', 'USER_ID_PARTITIONS_COLUMN'):
        column_name = kwargs[key]
        if column_name in df.columns:
            partition_cols.append(column_name)
    if len(partition_cols) == 0:
        raise ValueError('No partition columns are found in data')

    setup_google_cloud_credentials()

    gcs_data_path = f'{kwargs["GCS_BUCKET"]}/{table_path_postfix}'
    gcs_fs = pa.fs.GcsFileSystem()

    pa_table = pa.Table.from_pandas(df)
    pq.write_to_dataset(pa_table, filesystem=gcs_fs, root_path=gcs_data_path,
                        partition_cols=partition_cols, existing_data_behavior='delete_matching')

    return {
        'prefix': f'gs://{gcs_data_path}',
        'paths': [f'gs://{path}' for path in pq.ParquetDataset(gcs_data_path, gcs_fs).files]
    }
