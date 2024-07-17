# Online Retail Data Processing Pipeline
This project demonstrates a multi-part process for setting up a real-time data pipeline for online retail data using AWS services. The pipeline includes setting up Kinesis, Glue, Data Firehose, transforming data with Glue Jobs, storing data in RDS, querying data with Athena, visualizing data with QuickSight, managing S3 lifecycles, creating IAM roles, and setting up continuous integration and deployment with AWS CodeBuild and CodePipeline.

## Table of Contents
1. Kinesis Setup
2. Glue Setup to Send Data to Kinesis
3. Setup Data Firehose
4. Glue Job for Transforming Stream Data into Cleansed Data
5. Create RDS Instance
6. Load Transformed Data to RDS
7. Setup Athena and KPIs
8. QuickSight and Visualizations
9. S3 Lifecycle
10. IAM Role
11. AWS CodeBuild
12. AWS CodePipeline

## Part 1: Kinesis Setup
1. Create a Kinesis Data Stream:
- Open the AWS Management Console.
- Navigate to Kinesis > Data Streams.
- Click "Create data stream".
- Enter the stream name (e.g., OnlineRetailDataStream).
- Specify the number of shards based on your expected data volume.
- Click "Create stream".

2. Enter Details:
- Give stream name.
- Choose "On-demand" or "Provisioned" as per requirement (On-demand is chosen here).
- Click "Create data stream".
- Check the status: Ensure it is Active.

## Part 2: Glue Setup to Send Data to Kinesis
1. Create a Python Shell Glue job:
- Create a Glue catalog for retail data that will be streamed.

2. Prepare Dataset:
- Ensure the dataset is in an S3 location from where you want to stream the data.
- Check Glue Catalog: Ensure the job succeeds and the Glue catalog is created.

3. Create a Python Shell Glue job to send data to Kinesis Stream:
- Use boto3 Client to connect to the Kinesis Stream.
- Provide the S3 location to send the data from.

4. Create Data Firehose:
- Once the job succeeds, proceed to create Data Firehose to get that data.

5. Monitor Data Arrival:
- Use the monitoring tab of Kinesis to check if the data has arrived.

## Part 3: Setup Data Firehose
1. Create Firehose Stream:
- Click "Create Firehose stream".
- Choose Source and Destination.
- Provide source stream.
- Provide the destination settings.

2. Provide IAM Role:
- Ensure proper IAM role to access S3 and Kinesis Data Stream.
- Check Firehose Status: Ensure Firehose is active, and it will transfer data from Kinesis Data Stream to the S3 destination in part files.

## Part 4: Glue Job for Transform Stream Data into Cleansed Data
1. Create Spark Glue Job:
- Store the data in an S3 location.
- Ensure the job succeeds and check the transformed data in S3.

## Part 5: Create RDS Instance
1. Create DB Instance:
- Go to RDS console and create a DB instance.
- Choose MySQL.
- Choose Free Tier.
- Provide DB instance name, username, and password.
- Keep other settings as default.
- Ensure the status is available once created.

## Part 6: Load Transformed Data to RDS
1. Create Spark Glue Job:
- Load S3 data to RDS.
- Provide connection details.

2. Verify Data Load:
- Use DBVisualizer to create a connection and check if the table is created.

## Part 7: Setup Athena and KPIs
1. Athena Console:
- Use the correct database and table.

2. Run aggregation KPI queries:
- Inventory Turnover Ratio
- Stockout Rate
- COGS to Revenue Ratio
- Customer Acquisition Cost (CAC)
- Returning Customers
- Average Order Value (AOV)
- Gross Margin

## Part 8: QuickSight and Visualizations
1. QuickSight Setup:
- Login to QuickSight.
- Choose the dataset for visualization.
- Click on "New Dataset" and choose RDS.
- Enter RDS details and test the connection.

2. Create Dashboard:
- Sum of Invoice total by invoice date.
- Sum of Quantity of Stockcode.
- Sum of invoice total by country.
- Number of items of Unitprice and Quantity.
- Sum of Invoicetotal, Sum of Quantity, and Sum of Unitprice by Month.
- Sum of Quantity by Month and Country.

## Part 9: S3 Lifecycle
1. Lifecycle Rule Setup:
- Go to Lifecycle Rule in Management of S3 bucket.
- Add rules and transitions.
- Include Glacier storage and permanent delete options.
- Review transition and expiration actions.

## Part 10: IAM Role
1. Create IAM Role:
- Go to IAM Role console.
- Click on "Roles" and create a new role.
- Choose AWS service and service to add permissions.
- Add necessary permissions to the role.

## Part 11: AWS CodeBuild
1. Create Project:
- Go to AWS CodeBuild console.
- Click "Create Project".
- Provide project details.
- Create a buildspec.yaml file and push it to GitHub.

**Note**: In the buildspec.yaml file, resources run are limited due to the cost constraints of recreating and running them.

- Click "Start build" and ensure proper IAM permissions.
- Check if the build succeeds.

## Part 12: AWS CodePipeline
1. Create Pipeline:
- Go to AWS CodePipeline console.
- Click "Create Pipeline".
- Provide pipeline details.
- Add source details.
- Add CodeBuild.
Ensure all stages are green.

![image](https://github.com/user-attachments/assets/3d5c0d13-8c20-4768-8c12-479faee89a7d)
