from google.cloud import bigquery

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from data_science_stack_exchange.utils.helpers.google_cloud import setup_google_cloud_credentials
from data_science_stack_exchange.utils.helpers.mage_env import load_config


@custom
def create_biquery_dataset(*args, **kwargs) -> dict:
    config = load_config()
    setup_google_cloud_credentials()

    project_id = kwargs['GCLOUD_PROJECT_ID']
    dataset_id = kwargs['BIGQUERY_DATASET_ID']
    full_dataset_id = f'{project_id}.{dataset_id}'
    dataset = bigquery.Dataset(full_dataset_id)
    dataset.location = config['GOOGLE_LOCATION']

    bq_client = bigquery.Client()
    assert bq_client.project == project_id
    bq_client.create_dataset(dataset, exists_ok=True)
    return {'full_dataset_id': full_dataset_id}


# test is not working for some reason
@test
def test_output(full_dataset_id_dict, *args) -> None:
    assert False
    # bq_client.get_dataset(full_dataset_id)
