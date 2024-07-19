# Interactive Exercise 1: Loading Data with PySpark

## Context:
In this exercise, you’ll learn how to start a PySpark session and load data into a Spark DataFrame. We’ll use a sample CSV file containing information about various products.

## Instructions:

1. Start a PySpark session.
2. Load the CSV data into a Spark DataFrame.

## Sample Code:

```python
# Step 1: Start a PySpark session
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Parallelizing Workloads with PySpark") \
    .getOrCreate()

# Step 2: Load the CSV data into a Spark DataFrame
file_path = "path/to/your/products.csv"  # replace with the actual file path
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Display the DataFrame schema
df.printSchema()
