import boto3

region_list = ["eu-west-2", "eu-west-1", "us-east-1"]

for region in region_list:
    print("REGION: ", region)
    config = boto3.client('config', region_name=region)
    recorders = config.describe_configuration_recorder_status()

    for record in recorders["ConfigurationRecordersStatus"]:
        print("Name: ", record["name"])
        print("is Recording: ", record["recording"])
        print("Status: ", record["lastStatus"])
    print("------------------------------------------------")

# channels = config.describe_delivery_channels()
#
# for channel in channels["DeliveryChannels"]:
#     print("Name: ", channel["name"])
#     print("Name: ", channel["configSnapshotDeliveryProperties"]["deliveryFrequency"])
# print("------------------------------------------------")
