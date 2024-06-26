from google.cloud import bigquery

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from data_science_stack_exchange.utils.helpers.google_cloud import setup_google_cloud_credentials


@custom
def transform_custom(*gcs_dicts, **kwargs) -> dict:
    setup_google_cloud_credentials()
    bq_client = bigquery.Client()
    dataset_ref = bq_client.dataset(kwargs['BIGQUERY_DATASET_ID'])

    table_names = {}
    for gcs_dict in gcs_dicts:
        if 'table_name' not in gcs_dict:
            continue
        table_name = gcs_dict['table_name']
        gcs_prefix = gcs_dict['prefix']

        assert table_name not in table_names

        table_ref = bigquery.TableReference(dataset_ref, f'{table_name}_external')
        external_config = bigquery.ExternalConfig(bigquery.ExternalSourceFormat.PARQUET)
        external_config.source_uris = [gcs_prefix + '/*']
        partitioning_options = bigquery.HivePartitioningOptions()
        partitioning_options.mode = 'AUTO'
        partitioning_options.source_uri_prefix = gcs_prefix
        external_config.hive_partitioning = partitioning_options

        table = bigquery.Table(table_ref)
        table.external_data_configuration = external_config
        table_ref = bq_client.create_table(table, exists_ok=True)
        table_names[table_name] = table_ref.table_id
    return table_names


@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
