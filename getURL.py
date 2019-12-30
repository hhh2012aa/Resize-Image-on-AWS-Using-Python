import json
import boto3
import botocore

def lambda_handler(event, context):
    # TODO implement
    Origin_URL = event['filename']
    Resized_URL = "Resized/Resized-" + Origin_URL
    s3 = boto3.resource('s3')
    
    try:
        s3.Object('55564p', Origin_URL).load()
        S3_site = "https://s3.console.aws.amazon.com/s3/object/55564p/"
        Origin_URL =  S3_site + Origin_URL 
        Resized_URL =  S3_site + Resized_URL
        return {
            "statusCode":200,
            "Origin_URL":   Origin_URL,
            "Resized_URL":  Resized_URL
        }
        
    except:
        return {
    
            "statusCode":404,
            "message":"Error, File is not exist.",
            
        }
