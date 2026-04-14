import boto3

ec2 = boto3.client("ec2")

# ec2.stop_instances(
#     InstanceIds=["i-0aaa4139a103b0874"]
# )

response = ec2.describe_instance_types (
    InstanceTypes=[
        't2.micro',
        't3.micro',
        'm5.large'
    ]
)
print(response)