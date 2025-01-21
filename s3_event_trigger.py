import boto3

class S3EventTrigger:
    def __init__(self, bucket_name, sns_topic_arn):
        self.bucket_name = bucket_name
        self.sns_topic_arn = sns_topic_arn
        self.s3 = boto3.client('s3')
        self.sns = boto3.client('sns')

    def trigger_event(self, file_name):
        print(f"Uploading file '{file_name}' to S3 bucket '{self.bucket_name}'...")
        self.s3.upload_file(file_name, self.bucket_name, file_name)
        print(f"File '{file_name}' uploaded successfully!")
        self.notify_via_sns(file_name)

    def notify_via_sns(self, file_name):
        message = f"File '{file_name}' has been uploaded to S3 bucket '{self.bucket_name}'."
        self.sns.publish(TopicArn=self.sns_topic_arn, Message=message)
        print(f"SNS notification sent: {message}")
