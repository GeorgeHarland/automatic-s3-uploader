from keys import access_key, secret_access_key

import boto3
import os

# pass in service we want to use + access keys
client = boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)

# Now have access to all s3 resources that the access key has access to

for file in os.listdir():
    if '.py' in file:
        upload_file_bucket = 'test-bucket1357'
        upload_file_key = 'python/' + str(file)
        client.upload_file(file,upload_file_bucket,upload_file_key)