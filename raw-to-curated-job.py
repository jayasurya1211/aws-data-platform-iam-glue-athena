from pyspark.context import SparkContext
from awsglue.context import GlueContext

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

df = spark.read \
    .option("header", "true") \
    .csv("/s3://company-data-lake-testdemo/raw/")

df.write \
    .mode("overwrite") 
    .parquet("s3://company-data-lake-testdemo/curated/")
