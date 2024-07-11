from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("Insert RDS Data and Write to S3").getOrCreate()

# Define the RDS connection options
rds_options = {
    "url": "jdbc:mysql://retaildb.cfgq6m64ewxm.us-east-1.rds.amazonaws.com:3306/retaildb",
    "user": "admin",
    "password": "capstoneproject",
    "driver": "com.mysql.cj.jdbc.Driver"
}


# Load data from S3
s3_path = "s3://ade-project/transformed_data/"
df_s3 = spark.read.csv(s3_path, header=True, inferSchema=True)
df_s3.show(5)

# Insert data into RDS
df_s3.write \
    .format("jdbc") \
    .options(**rds_options) \
    .option("dbtable", "online_retail") \
    .mode("overwrite") \
    .save()

# Stop the Spark session
spark.stop()
