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
