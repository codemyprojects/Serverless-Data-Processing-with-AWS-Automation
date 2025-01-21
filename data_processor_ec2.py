import subprocess

class DataProcessorEC2:
    def __init__(self, instance_id):
        self.instance_id = instance_id

    def start_processing(self):
        print(f"Simulating data processing on EC2 instance '{self.instance_id}'...")
        # Replace this with actual EC2 processing logic
        subprocess.run(["echo", "Processing data on EC2..."])
        print("Data processing completed.")
