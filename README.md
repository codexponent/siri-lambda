[![Build Status](https://dev.azure.com/sulabhshrestha/siri-lambda/_apis/build/status/GitHub/siri-lambda?branchName=main)](https://dev.azure.com/sulabhshrestha/siri-lambda/_build/latest?definitionId=1&branchName=main)

# Siri-Lambda
Connecting Siri with AWS Lambda to turn on/off the VM's

<br/>

# Architecture
<img align="center" alt="Photo" src="./architecture.png" />

# Motivation
This project is created to turn on the AWS EC2 Machines from your voice assistance (Siri). For this project I have used AWS Lambda function to invoke the start/stop function for the Instances, triggered by the API Gateway which is called through Siri. I am also using Docker images  rather than the script to put in into the serverless architrecture and using DockerHub as the Registry for backup and ECR for Lambda to get the docker images directly. I also have implemented AzureDevOps in this project to make it easier to change the function through the code push into the GitHub.

# Tools
- AWS EC2 Instance: 
- AWS Lambda Function
- API Gateway
- AWS Elastic Container Registry
- Docker
- Siri
- Azure DevOps
- Docker Hub Registry
- 

# How to Use