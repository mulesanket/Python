import boto3

iam = boto3.client('iam')

response = iam.list_users()
users = response["Users"]

for user in users:
    print(user["UserName"])

