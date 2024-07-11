import boto3
import json
import csv

# Initialize boto3 clients
s3_client = boto3.client('s3')
kinesis_client = boto3.client('kinesis', region_name='us-east-1')  # Update region as needed

# Parameters
s3_bucket = "ade-project"
s3_key = "dataset/Online_Retail.csv"
kinesis_stream_name = "OnlineRetailDataStream"

# Function to process CSV file from S3 and send records to Kinesis
def process_csv_and_send_to_kinesis(s3_bucket, s3_key, kinesis_stream_name):
    # Download CSV file from S3
    obj = s3_client.get_object(Bucket=s3_bucket, Key=s3_key)
    csv_data = obj['Body'].read().decode('utf-8').splitlines()
    
    # Parse CSV and send records to Kinesis
    csv_reader = csv.DictReader(csv_data)
    record_count = 0
    
    for row in csv_reader:
        # Transform row to JSON string
        record = json.dumps(row)
        
        # Send record to Kinesis stream
        kinesis_client.put_record(
            StreamName=kinesis_stream_name,
            Data=record,
            PartitionKey=row['InvoiceNo']  # Assuming 'InvoiceNo' is the partition key
        )
        
        record_count += 1
        
        # Print a message every 100 records processed
        if record_count % 100 == 0:
            print(f"Processed {record_count} records")
    
    print(f"Total records processed: {record_count}")

# Execute function to process CSV and send to Kinesis
process_csv_and_send_to_kinesis(s3_bucket, s3_key, kinesis_stream_name)
