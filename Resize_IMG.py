import json
import boto3
from PIL import Image
import logging
import tempfile


def resize_1(input_file, key):
    im = Image.open(input_file)
    x_s = 640 
    y_s = 360 
    out = im.resize((x_s,y_s),Image.ANTIALIAS) 
    out.save('/tmp/new_'+ key)
    

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    
    s3.download_file(bucket, key, '/tmp/' + key)

    resize_1('/tmp/'+ key, key)
    logging.error(event)
    try:
        if key[0:7] != 'Resized':
            s3.upload_file('/tmp/new_'+ key , bucket,  'Resized/Resized-'+ key)
            logging.error('Already Resized')
    except:
        logging.error('Error')
        return{
            code:404,
            status:"error",
            message:"unauthorized token"
            }
   
   
   
   
    return {
        "statusCode": 200,
        "body": json.dumps("Successed")
    }
