# Serverless-Data-Processing-with-AWS-Automation
S3 Data Processing Automation
Introduction

This project automates the handling of data files for Workman’s analytics platform using Amazon Web Services (AWS). The primary objective is to simplify the process of uploading, processing, and retrieving data with minimal manual intervention. The system utilizes AWS services such as Amazon S3 for storage, EC2 for processing, and SNS for notifications, ensuring that the entire data handling workflow is efficient, secure, and scalable.
Key Features

Data Upload: 
Users can upload CSV data files to Amazon S3 via the AWS console or other upload tools. The system ensures that data follows the required naming conventions and encoding.

Automated Data Processing: 
Once data is uploaded to S3, an EC2 instance is triggered to process the data. This process runs during specified business hours to ensure optimal resource usage.

Notification System: 
Once processing is complete, Amazon SNS sends notifications to users about the success or failure of the data processing tasks.

Data Retrieval: 
Processed data is stored back in S3, where users can easily download the results.

This document outlines the process for automating the handling of S3 data for Workman’s new analytics platform. The main goal is to simplify the use of data for analysis while allowing for future feature enhancements.

1.1 Overview of S3 Automated Data Handling Process

    The process enables users to upload data and trigger automatic processing in Amazon S3.
    Workflow Diagram Explanation:
        Data Registering User: Uploads target data and trigger files to Amazon S3.
        Amazon S3: Stores uploaded data.
        Amazon EC2: Automatically processes the data.
        Amazon SNS: Sends notifications when processing is complete.
        Data User: Downloads processed data from S3.

    Main Features:
        Upload analysis data to S3 (using AWS Console or upload tools).
            Data must be in CSV format.
            File naming rules:
                English characters only.
                Encoding: Shift-JIS (Microsoft Code Page 932).
                Header row required for data formatting.

        Processed data is saved back to S3.
            Trigger files initiate processing.
            Notifications are sent after data processing.

1.2 Constraints of Automated Data Handling

    Access Restrictions:
        Access requires AWS IAM credentials.
        Only accessible from within the Workman network.
        Prevents unauthorized processing by third parties.
    Non-Real-Time Processing:
        Processing might have delays depending on the data size.
    Operation Hours:
        Processing operates only during business hours (9 AM to 6 PM) but can be adjusted temporarily.

