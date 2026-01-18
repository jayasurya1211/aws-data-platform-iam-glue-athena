
# AWS Data Platform – IAM, S3, Glue, Athena (v3)

## Overview
This project implements a production-style AWS data platform using
IAM, Amazon S3, AWS Glue, and Amazon Athena, enhanced with partitioning
and job parameterization for performance and reuse.

---

## Architecture
IAM (Users & Groups)
|
v
S3 (Raw Zone)
|
v
AWS Glue ETL (Parameterized)
|
v
S3 (Curated Zone – Parquet, Partitioned)
|
v
Amazon Athena (Optimized SQL)


---

## IAM Design
- **Data Engineer**: Glue jobs, S3 read/write, Athena metadata
- **Data Analyst**: Read-only access to curated data, Athena queries
- **DevOps**: Administrative access

Policies follow least-privilege and group-based access.

---

## Data Flow
1. CSV data lands in S3 `raw/`
2. Parameterized Glue job reads input path
3. Data is written as **partitioned Parquet**
4. Athena queries curated partitions efficiently

---

## AWS Glue ETL (v2)
- Glue 4.0, PySpark
- Runtime parameters:
  - `--input_path`
  - `--output_path`
- Output partitioned (e.g., by `age`)
- No hard-coded S3 paths

---

## Partitioning & Optimization
- Parquet data partitioned to reduce Athena scan size
- Partitions loaded with:
  ```sql
  MSCK REPAIR TABLE

  ## Monitoring & Alerts
- CloudWatch alarm configured for AWS Glue job failures
- Alarm triggers when ETL job execution fails
- Optional SNS email notification for alerts

