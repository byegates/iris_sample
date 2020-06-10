from google.cloud import bigquery
client = bigquery.Client()
filename = './iris.csv'
dataset_id = 'iris'
table_id = 'iris_tbl'
project = "onyx-stack-274706"

dataset_ref = client.dataset(dataset_id, project)
table_ref = dataset_ref.table(table_id)
job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.CSV
job_config.skip_leading_rows = 0
job_config.autodetect = True
job_config.replace = True

with open(filename, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_ref, job_config=job_config)

        job.result()  # Waits for table load to complete.

        print(f"Loaded {job.output_rows} rows into {dataset_id}:{table_id}.")
