import boto3

class SNSNotifier:
    def __init__(self, sns_topic_arn):
        self.sns_topic_arn = sns_topic_arn
        self.sns = boto3.client('sns')

    def send_notification(self, message):
        print(f"Sending SNS notification: {message}")
        self.sns.publish(TopicArn=self.sns_topic_arn, Message=message)
        print("SNS notification sent successfully!")
