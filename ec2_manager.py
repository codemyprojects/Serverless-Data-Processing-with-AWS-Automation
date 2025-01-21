import boto3

class EC2Manager:
    def __init__(self, instance_id):
        self.instance_id = instance_id
        self.ec2 = boto3.client('ec2')

    def start_instance(self):
        print(f"Starting EC2 instance '{self.instance_id}'...")
        self.ec2.start_instances(InstanceIds=[self.instance_id])
        print(f"EC2 instance '{self.instance_id}' started.")

    def stop_instance(self):
        print(f"Stopping EC2 instance '{self.instance_id}'...")
        self.ec2.stop_instances(InstanceIds=[self.instance_id])
        print(f"EC2 instance '{self.instance_id}' stopped.")
