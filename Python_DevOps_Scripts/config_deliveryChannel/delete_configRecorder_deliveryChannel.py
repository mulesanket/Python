import boto3

regions = ["us-east-1", "eu-west-2", "eu-west-1"]

for region in regions:

    print("\nRegion:", region)

    config = boto3.client("config", region_name=region)

    # Get configuration recorders
    recorders = config.describe_configuration_recorders()

    # Stop configuration recorders
    for recorder in recorders["ConfigurationRecorders"]:
        recorder_name = recorder["name"]

        config.stop_configuration_recorder(
            ConfigurationRecorderName=recorder_name
        )

        print("Stopped recorder:", recorder_name)


    # Get delivery channels
    channels = config.describe_delivery_channels()

    # Delete delivery channels
    for channel in channels["DeliveryChannels"]:
        channel_name = channel["name"]

        config.delete_delivery_channel(
            DeliveryChannelName=channel_name
        )

        print("Deleted delivery channel:", channel_name)


    # Delete configuration recorders
    for recorder in recorders["ConfigurationRecorders"]:
        recorder_name = recorder["name"]

        config.delete_configuration_recorder(
            ConfigurationRecorderName=recorder_name
        )

        print("Deleted recorder:", recorder_name)