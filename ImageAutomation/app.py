import os
import json
import boto3
import zipfile
import json
import os
import tempfile
import logging
from datetime import datetime
from boto3.dynamodb.conditions import Key

s3 = boto3.client('s3')
# Set the root logger level to INFO
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def write_item_to_dynamodb(table_name, item, region_name='us-east-1'):
    """
    Write an item to a DynamoDB table.

    :param table_name: Name of the DynamoDB table
    :param item: A dictionary representing the item to write
    :param region_name: AWS region (default: us-east-1)
    :return: Response from DynamoDB or None on error
    """
    dynamodb = boto3.resource('dynamodb', region_name=region_name)
    table = dynamodb.Table(table_name)

    try:
        response = table.put_item(Item=item)
        logger.info(f"Successfully wrote item to {table_name}: {item}")
        return response
    except ClientError as e:
        logger.error(f"Failed to write item to {table_name}: {e}")
        return None


def lambda_handler(event, context):
    # masrikdahir_image_place
    try:
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        object_key = event['Records'][0]['s3']['object']['key']
        logger.info(f"[Bucket Name] {bucket_name}, [Object Key] {object_key}")

        iso_timestamp = datetime.utcnow().isoformat() + "Z"
        dt = datetime.fromisoformat(iso_timestamp.rstrip("Z"))
        day = dt.day
        month = dt.month
        year = dt.year

        try:
            write_item_to_dynamodb(
                table_name="masrikdahir_image_place",
                item={
                    "timestamp": str(year)+str(month)+str(day),
                    "place": object_key
                }
            )
        except Exception as e:
            logger.error(f"Unable write data to DynamoDB: {e}")

    except Exception as e:
        logger.error(f"Unable to get data from S3: {e}")
        return {
            'statusCode': 500,
            'body': "Unable to get data from S3"
        }
    return {
        'statusCode': 200,
        'body': "Success"
    }

