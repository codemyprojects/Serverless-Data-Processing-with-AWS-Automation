import boto3

class S3DataManager:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.s3 = boto3.client('s3')

    def download_file(self, file_name, local_path):
        print(f"Downloading file '{file_name}' from S3 bucket '{self.bucket_name}' to '{local_path}'...")
        self.s3.download_file(self.bucket_name, file_name, local_path)
        print(f"File '{file_name}' downloaded successfully!")

    def upload_file(self, file_name, local_path):
        print(f"Uploading file '{local_path}' to S3 bucket '{self.bucket_name}' as '{file_name}'...")
        self.s3.upload_file(local_path, self.bucket_name, file_name)
        print(f"File '{file_name}' uploaded successfully!")
