from s3_event_trigger import S3EventTrigger
from data_processor_ec2 import DataProcessorEC2
from s3_data_manager import S3DataManager
from sns_notifier import SNSNotifier
from ec2_manager import EC2Manager

def main():
    # Configuration
    bucket_name = "your-s3-bucket"
    sns_topic_arn = "your-sns-topic-arn"
    ec2_instance_id = "your-ec2-instance-id"
    file_to_upload = "test.csv"
    local_download_path = "downloaded_test.csv"

    # Initialize classes
    s3_trigger = S3EventTrigger(bucket_name, sns_topic_arn)
    ec2_processor = DataProcessorEC2(ec2_instance_id)
    s3_manager = S3DataManager(bucket_name)
    sns_notifier = SNSNotifier(sns_topic_arn)
    ec2_manager = EC2Manager(ec2_instance_id)

    # Workflow
    s3_trigger.trigger_event(file_to_upload)
    ec2_manager.start_instance()
    ec2_processor.start_processing()
    ec2_manager.stop_instance()
    s3_manager.download_file(file_to_upload, local_download_path)
    sns_notifier.send_notification("Workflow completed successfully.")

if __name__ == "__main__":
    main()
