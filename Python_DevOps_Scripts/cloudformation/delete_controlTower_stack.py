import boto3

regions = [
    "us-east-1",
    "eu-west-1",
    "eu-west-2"
]

stack_prefix = "StackSet-AWSControlTower"


for region in regions:

    print("\nChecking region:", region)

    cloudformation = boto3.client(
        "cloudformation",
        region_name=region
    )

    stacks = cloudformation.list_stacks()

    for stack in stacks["StackSummaries"]:

        stack_name = stack["StackName"]
        stack_status = stack["StackStatus"]

        if stack_name.startswith(stack_prefix) and stack_status != "DELETE_COMPLETE":

            print("Deleting:", stack_name)

            cloudformation.delete_stack(
                StackName=stack_name
            )

            print("Delete started:", stack_name)