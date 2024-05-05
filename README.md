# Data Engineering project for Data Engineering Zoomcamp

This is a final project for Data Engineering Zoomcamp 2024. It uses open data from [Data Science Stack Exchange](https://datascience.stackexchange.com/). The data for this and other stack exchange / stack overflow sites can be downloaded from [archive.org](https://archive.org/download/stackexchange). Project dashboard can be found [here](https://lookerstudio.google.com/reporting/cd6dfa82-45f9-4654-b4ce-887da885fd15).

The project uses following technologies:
- Mage as an orchestrator
- Docker + Docker Compose for deploying a Mage instance
- Google Cloud Storage for storing a data lake
- Google BigQuery for data warehousing
- dbt + BigQuery for batch data processing
- Looker Studio for data visualization

## Project description

Mage project structure can be seen in the following diagram:
![mage project diagram](https://github.com/tsbalzhanov/DataEnginieeringZoomcamp_DataScienceStackExchange/blob/main/readme/mage_project_graph.png?raw=true)

Block descriptions:
- `download_and_unpack_archive` - download archive with data, and unpacks its content into a working directory
- `load_comments`, `load_posts`, `load_users`, `load_votes` - load xml file into a dataframe and parse datetime columns
- `add_partition_column_to_comments`, `add_partition_column_to_posts` `add_partition_column_to_users`, `add_partition_column_to_votes` - add partition columns to dataframes
- `export_comments_to_gcs`, `export_posts_to_gcs`, `export_users_to_gcs`, `export_votes_to_gcs` - export data as partitioned tables in GCS
- `create_bigquery_dataset` - create BigQuery dataset unless it already exists
- `create_bigquery_external_gcs_tables` - create external BigQuery tables
- `seed_vote_types` - create BigQuery table with vote types via dbt seed
- `comments`, `posts`, `users`, `votes` - create materialized BigQuery tables from corresponding external tables and convert datetime columns
- `top_commenters`, `top_posters` - calculate top all-time commenters and posters by number of comments and posts respectively
- `vote_type_stats` - calculate vote type counts with a dbt model
- `daily_post_and_comments_stats` - calculate daily counts of posts and comments

### Table partitining

Tables are paritioned by remainder of post id and / or user id after division by number of corresponding partitions (16 and 16 by default). This is done because post id and user id are the most important ids in the dataset and majority of joins will be done via these two ids. Therefore, is these remainders are used for such joins, they will make them less resource intensive because sql executor will know where to look for corresponding ids in the partitioned data.

### Dashboard

Dashboard can be found [here](https://lookerstudio.google.com/reporting/cd6dfa82-45f9-4654-b4ce-887da885fd15).

It's made manually in Looker Studio employing its BigQuery connections. The dashboard has 4 panels with:
- A table with all-time most prolific commenters
- A table with all-time most prolific posters
- A pie chart with all-time vote type count distribution
- A time series chart with daily number of posts and comments for march 2024

## How to reproduce
Requirements:
- Installed Docker Compose
- Google Cloud account

1. Get & copy Google Cloud credentials json file into a subdirectory
```bash
mkdir credentials
cp $GOOGLE_CREDENTIALS_FILE credentials/google_cloud_credentials.json
```
2. Clone the repo into another subdirectory and change directory into it
```bash
git clone https://github.com/tsbalzhanov/DataEnginieeringZoomcamp_DataScienceStackExchange.git
cd DataEnginieeringZoomcamp_DataScienceStackExchange
```
3. Change GCS / BigQuery variables (location, bucket, project, dataset) in following files:
- `data_science_stack_exchange/io_config.yaml`
- `data_science_stack_exchange/pipelines/data_science_stack_exchange/metadata.yaml`
- `data_science_stack_exchange/dbt/ds_se/profiles.yml`
4. Build and launch docker container
```bash
docker compose pull
docker compose build
docker compose up
```
5. Visit Mage UI at http://localhost:6789/ and launch a project instance

## Certificate

[Link to certificate](https://certificate.datatalks.club/dezoomcamp/2024/4b498edaa4a302a319d10d18542ef3130e449f3d.pdf)

Certificate id: `4b498edaa4a302a319d10d18542ef3130e449f3d`
