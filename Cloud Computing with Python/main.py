import json
import boto3
import io
from io import BytesIO

# retrieving access keys
credentials = {}
with open('credentials.json', 'rt') as file:
   credentials = json.load(file)

# accessing aws bucket
s3 = boto3.resource(
    service_name='s3',
    region_name='sa-east-1',
    aws_access_key_id=credentials['awsKEY_ID'],
    aws_secret_access_key=credentials['awsKEY'],
)

bucket = 'pedr9vskcray-pycourse-bucket'
prefix = 'imagens/'

# using object filter to traverse the bucket
for object_s3 in s3.Bucket(bucket).objects.filter(Prefix=prefix):
    if object_s3.key.endswith('jpg') or object_s3.key.endswith('png'):
        filename = object_s3.key.split('/')[1]
        print(filename)

# downloading the files inside the bucket
for object_s3 in s3.Bucket(bucket).objects.filter(Prefix=prefix):
    if object_s3.key.endswith('jpg') or object_s3.key.endswith('png'):
        
        # saving the filename of each object inside the bucket
        filename = object_s3.key.split('/')[1]
        # downloading the body of each object inside the bucket
        body = object_s3.get()['Body'].read()
        # transforming the bytes back into images
        imagem = io.BytesIO(body)

        with open(filename, 'wb') as file:
            file.write(imagem.getbuffer())
