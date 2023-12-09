import boto3

file_name = './balance_sheet.png'
bucket = 'ai-demo-fast'
key_name = 'balance_sheet.png'

# Opens Client
client = boto3.client('s3', 'us-east-1')
# Transfer file with boto3 API
transfer = boto3.s3.transfer.S3Transfer(client=client)
transfer.upload_file(file_name,
                     bucket, 
                     key_name
)