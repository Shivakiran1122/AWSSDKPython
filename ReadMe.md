**Over View:**
1.This project is basically using Boto3( AWS SDK for python) in VS Code on windows to connect to AWS S3 buckets.
2.Boto3 is python library to interact with all aws services.In AWS S3 is a simple storage service where you can store structured , Semi structured and Unstructured Data.

**Installtion steps:**
1. Install boto3 using pip command: pip install boto3

2. Configure the credientals using AWS CLI For Windows<br/>
   **Step1**.Download and run the AWS CLI MSI installer for Windows (64-bit):<br/>
   https://awscli.amazonaws.com/AWSCLIV2.msi<br/>
   **Step2**.To confirm the installation, open the Start menu, search for cmd to open a command prompt window, and at the command prompt use the<br/>
    aws --version command<br/>
    
3. To access AWS services with the AWS CLI<br/>
   **Step1:** Sign up to AWS<br/>
   **Step2:** Create an IAM user account<br/>
   **Step3:** Create an access key ID and secret access key<br/>

4. Open command prompt and type:
   **Step1:** aws configure<br/>
     AWS CLI prompts you for four pieces of information:<br/>
     **1**.Access key ID<br/>
     **2**.Secret access key<br/>
     **3**.AWS Region<br/>
     **4**.Output format : **1.** If you don't specify an output format, json is used as the default.<br/>
                           **2.** Json,Yaml,Text,Table output format may be any one of these<br/>
                       
5. The AWS CLI stores sensitive credential information that you specify with aws configure in a local file named credentials, in a folder named .aws in your home directory.
  
 6.The less sensitive configuration options that you specify with aws configure are stored in a local file named config, also stored in the .aws folder in your home directory.

**Operations performed using BOTO3:**
1. List all the buckets
2. List all the objects inside the bucket
3. Upload files to bucket
4. Downloading file
5. Download  file with binary data
6. Presigned url to give limited access  to an unauthorized user
7. Create Bucket
8. Copy objects to other bucket
9. Get Object
 
