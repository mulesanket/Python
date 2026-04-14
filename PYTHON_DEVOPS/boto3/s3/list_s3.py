import boto3

my_s3 = boto3.client("s3")

response = my_s3.list_buckets()

for bucket in response:
    bucketName = bucket["Buckets"]
    print(bucketName["Name"])
