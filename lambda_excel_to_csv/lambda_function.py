import boto3
import pandas as pd
from io import BytesIO
import os
import urllib.parse

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    destination_bucket = 'csv-bucket-to-snowflake-o'

    response = s3_client.get_object(Bucket=source_bucket, Key=object_key)
    file_content = response['Body'].read()

    base_filename = os.path.splitext(os.path.basename(object_key))[0]
    excel_file = pd.ExcelFile(BytesIO(file_content))

    for sheet_name in excel_file.sheet_names:
        df = excel_file.parse(sheet_name)
        csv_buffer = BytesIO()
        df.to_csv(csv_buffer, index=False)

        sanitized_sheet = "".join(c if c.isalnum() or c in ['-', '_'] else '_' for c in sheet_name)
        csv_filename = f"{base_filename}_{sanitized_sheet}.csv"

        s3_client.put_object(
            Bucket=destination_bucket,
            Key=csv_filename,
            Body=csv_buffer.getvalue()
        )

    return {
        'statusCode': 200,
        'body': f"{len(excel_file.sheet_names)} CSVs created from {object_key}"
    }
