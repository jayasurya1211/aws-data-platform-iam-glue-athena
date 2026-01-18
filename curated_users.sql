CREATE EXTERNAL TABLE curated_users (
  id string,
  name string,
  age string
)
STORED AS PARQUET
LOCATION 's3://company-data-lake-testdemo/curated/';
