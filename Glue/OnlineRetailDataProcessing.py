import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import IntegerType, FloatType

# Initialize Spark and Glue context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Parameters
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
output_path = "s3://ade-project/transformed_data/"

# Load JSON data directly into a DataFrame from all subdirectories
json_data = spark.read.json("s3://ade-project/stream_data/2024/07/08/*")

# Select columns and cast types as needed
df = json_data.selectExpr("InvoiceNo", "StockCode", "Description", 
                          "cast(Quantity as int) Quantity", 
                          "InvoiceDate", 
                          "cast(UnitPrice as float) UnitPrice", 
                          "cast(CustomerID as string) CustomerID", 
                          "Country")

# Show schema and sample data
print("Schema of the DataFrame:")
df.printSchema()
print("Sample data:")
df.show(5)

# Data Cleaning
print("Starting Data Cleaning...")

# Drop rows with missing values in critical columns
df_cleaned = df.dropna(subset=["InvoiceNo", "StockCode", "Description", "Quantity", "InvoiceDate", "UnitPrice", "CustomerID", "Country"])

# Remove duplicates
df_cleaned = df_cleaned.dropDuplicates()

# Data Transformation
print("Starting Data Transformation...")

# Define a function to parse date in multiple formats
def parse_date(date_str):
    try:
        return to_timestamp(date_str, "M/d/yyyy H:mm")
    except ValueError:
        try:
            return to_timestamp(date_str, "M/d/yyyy HH:mm")
        except ValueError:
            return None

# Extract date substring and parse it
df_transformed = df_cleaned.withColumn("InvoiceDate", parse_date(col("InvoiceDate")))

# Perform type casting for Quantity and UnitPrice
df_transformed = df_transformed.withColumn("Quantity", col("Quantity").cast(IntegerType())) \
                               .withColumn("UnitPrice", col("UnitPrice").cast(FloatType()))

# Calculate InvoiceTotal
df_transformed = df_transformed.withColumn("InvoiceTotal", col("Quantity") * col("UnitPrice"))

# Extract year, month, and day of month
df_transformed = df_transformed.withColumn("Year", year(col("InvoiceDate"))) \
                               .withColumn("Month", month(col("InvoiceDate"))) \
                               .withColumn("DayOfMonth", dayofmonth(col("InvoiceDate")))

# Print transformed data
print("Printing transformed data:")
df_transformed.show(5, truncate=False)

# Write the transformed data back to S3 in CSV format
print(f"Writing transformed data to S3: {output_path}")
df_transformed.write.mode("overwrite").option("header", "true").csv(output_path)

# End the Glue job
print("Glue job completed successfully")
