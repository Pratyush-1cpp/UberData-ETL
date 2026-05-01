# 🚀 Uber ETL Pipeline (PostgreSQL + Python)

## 📌 Overview

This project demonstrates a **complete ETL (Extract, Transform, Load) pipeline** built using Python and PostgreSQL.

The pipeline ingests raw Uber trip data, performs data cleaning and feature engineering, and loads the processed data into a relational database for analysis.

---

## 🎯 Objectives

* Build a **modular ETL pipeline**
* Practice **data cleaning & transformation**
* Load data into **PostgreSQL**
* Follow **production-style project structure**

---

## 🏗️ Architecture

```
Raw CSV → Extract → Transform → Load → PostgreSQL
```

---

## 📁 Project Structure

```
uber_etl_pipeline/
│
├── data/
│   └── uber.csv
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── output/
│
├── config.py
└── README.md
```

---

## ⚙️ Tech Stack

* Python (Pandas)
* PostgreSQL
* SQLAlchemy
* VS Code

---

## 🔄 ETL Pipeline Steps

### 1. Extract

* Reads raw data from CSV file

### 2. Transform

* Converts datetime columns
* Handles missing values
* Removes invalid records
* Creates new features:

  * year
  * month
  * hour

### 3. Load

* Loads processed data into PostgreSQL table (`uber_data`)

---

## 🧪 How to Run

### 1. Install dependencies

```
pip install pandas sqlalchemy psycopg2
```

### 2. Setup PostgreSQL

Create a database:

```sql
CREATE DATABASE uber_db;
```

### 3. Configure DB connection

Update `config.py`:

```python
DB_CONFIG = {
    "user": "postgres",
    "password": "your_password",
    "host": "localhost",
    "port": "5432",
    "database": "uber_db"
}
```

---

### 4. Run the pipeline

```
python -m src.main
```

---

## 🔍 Verify Data

Run in PostgreSQL:

```sql
SELECT * FROM uber_data LIMIT 10;
```

---

## 📊 Features Created

* `year` → Extracted from pickup datetime
* `month` → Extracted from pickup datetime
* `hour` → Extracted from pickup datetime

---

## 🧠 Key Learnings

* Designing **modular ETL pipelines**
* Handling **real-world messy data**
* Working with **databases in Python**
* Understanding **data flow architecture**

---

## 🚀 Future Improvements

* Add logging system
* Add data validation checks
* Use Airflow for orchestration
* Scale pipeline using Spark
* Store raw/processed data in AWS S3

---

## 👨‍💻 Author

Pratyush Nath Tripathi

---

## ⭐ Notes

This project is part of a structured **Data Engineering learning journey**, focusing on building real-world systems step by step.
