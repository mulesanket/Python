import boto3

ec2 = boto3.client("ec2")

ec2.stop_instances(
    InstanceIds=["i-0aaa4139a103b0874"]
)