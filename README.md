# AWS Data Platform – IAM, S3, Glue, Athena (v1)

## Overview
This project demonstrates a **production-style AWS data platform** built using
**IAM, Amazon S3, AWS Glue, and Amazon Athena**.

The focus of v1 is to design and implement:
- Secure, least-privilege IAM access
- An S3-based data lake
- ETL using AWS Glue
- Analytics using Amazon Athena
- End-to-end validation with real execution

---

## Architecture

IAM (Users & Groups)
|
v
S3 (Raw Zone)
|
v
AWS Glue ETL Job
|
v
S3 (Curated Zone - Parquet)
|
v
Amazon Athena (SQL Analytics)


---

## IAM Design

### Roles Implemented
- **Data Engineer**
  - Read/write access to S3 data lake
  - Permission to run Glue jobs
  - Create Athena databases and tables
- **Data Analyst**
  - Read-only access to curated S3 data
  - Permission to run Athena queries
- **DevOps**
  - Full administrative access (IAM & infrastructure)

### Security Best Practices
- Group-based permissions (no direct user permissions)
- Custom IAM policies for engineers and analysts
- MFA enabled for all users
- Least-privilege access enforced

IAM policies are stored in the `iam/` directory.

---

## Data Flow (v1)

1. Raw CSV data is uploaded to Amazon S3 (`raw/`)
2. AWS Glue job reads raw data
3. Data is transformed and written as **Parquet**
4. Curated data is stored in Amazon S3 (`curated/`)
5. Amazon Athena queries curated Parquet data

---

## AWS Glue ETL

- **Glue Version:** 4.0  
- **Language:** Python (PySpark)
- **Input:** CSV files from S3 raw zone
- **Output:** Parquet files in S3 curated zone

### Real-World Debugging
The Glue job initially failed due to a Glue 4.0 API mismatch.
The issue was identified using CloudWatch logs and resolved by updating the script
to align with Glue 4.0 execution behavior.

---

## Amazon Athena Analytics

- Athena external tables created on curated Parquet data
- SQL queries used for:
  - Data validation
  - Filtering
  - Aggregations
- Analyst access validated using least-privilege IAM policies

---

## Validation & Proof

This project includes real execution evidence:
- Successful Glue job runs
- Parquet files present in the curated S3 path
- Athena queries returning expected results

Screenshots are available in the `screenshots/` directory.

---

## Technologies Used
- AWS IAM
- Amazon S3
- AWS Glue
- Amazon Athena
- Amazon CloudWatch

---

## Key Takeaways
- IAM and S3 permissions must align for console access
- Glue jobs run using service roles, not IAM users
- Athena is schema-on-read and sensitive to table location and schema
- Debugging and validation are core parts of data engineering

---

## Project Status
**Version:** v1  
**Scope:** Secure data ingestion, transformation, and analytics using AWS managed services.



