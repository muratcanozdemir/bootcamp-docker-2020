import os
import boto3

dynamo_client = boto3.client(
        'dynamodb',
        endpoint_url='http://dynamodb:8000',
        region_name=os.environ.get('AWS_DEFAULT_REGION', 'us-west-2'),
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID', ''),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY', '')
    )

def get_items():
    return dynamo_client.scan(
        TableName=os.environ.get('TABLE_NAME', 'TestTable')
    )
