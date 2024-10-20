import json
import boto3

def lambda_handler(event, context):
    # Get the S3 client
    s3 = boto3.client('s3')
    
    # Log the received event
    print("Received event: " + json.dumps(event, indent=2))
    
    # Get bucket name and object key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    # Process the uploaded image (example: just log the details)
    print(f"Processing image from bucket: {bucket_name}, key: {object_key}")
    
    # Here, you can add any processing logic you need, such as resizing or analyzing the image.
    
    return {
        'statusCode': 200,
        'body': json.dumps('Image processed successfully!')
    }
