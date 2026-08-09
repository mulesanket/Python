import boto3

regions = ["us-east-1", "eu-west-2", "eu-west-1"]

for region in regions:

    print("\nRegion:", region)

    config = boto3.client("config", region_name=region)

    # Configuration Recorder Status
    recorders = config.describe_configuration_recorder_status()

    for recorder in recorders["ConfigurationRecordersStatus"]:
        print("Recorder Name:", recorder["name"])
        print("Running:", recorder["recording"])

    # Delivery Channel Status
    channels = config.describe_delivery_channel_status()

    for channel in channels["DeliveryChannelsStatus"]:
        print("Delivery Channel Name:", channel["name"])

        delivery_info = channel.get("configSnapshotDeliveryInfo", {})
        status = delivery_info.get("lastStatus", "No Status")

        print("Delivery Status:", status)