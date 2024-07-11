import boto3

# Initialize Glue client
glue_client = boto3.client('glue')

# Define parameters
database_name = 'online_retail_db'
table_name = 'online_retail_test'
s3_path = 's3://ade-project/dataset/Online_Retail_test.csv'

# Define table schema
table_input = {
    'Name': table_name,
    'StorageDescriptor': {
        'Columns': [
            {'Name': 'InvoiceNo', 'Type': 'string'},
            {'Name': 'StockCode', 'Type': 'string'},
            {'Name': 'Description', 'Type': 'string'},
            {'Name': 'Quantity', 'Type': 'int'},
            {'Name': 'InvoiceDate', 'Type': 'string'},
            {'Name': 'UnitPrice', 'Type': 'float'},
            {'Name': 'CustomerID', 'Type': 'string'},
            {'Name': 'Country', 'Type': 'string'}
        ],
        'Location': s3_path,
        'InputFormat': 'org.apache.hadoop.mapred.TextInputFormat',
        'OutputFormat': 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat',
        'SerdeInfo': {
            'SerializationLibrary': 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
        }
    }
}

# Create table in Glue Data Catalog
response = glue_client.create_table(
    DatabaseName=database_name,
    TableInput=table_input
)

print(f"Table '{table_name}' created successfully in database '{database_name}' with location '{s3_path}'.")
