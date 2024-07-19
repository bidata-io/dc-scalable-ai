# Chapter 4 Capstone Exercise

## Context

Congratulations on reaching the final exercise of the course! In this capstone exercise, you will deploy an AI model to Google Cloud Platform (GCP), set up monitoring to track its performance, and ensure it can scale based on demand. You will use Google AI Platform to deploy a pre-trained model, Google Cloud Monitoring to monitor the system, and configure auto-scaling to handle varying workloads. This exercise will integrate all the skills you’ve learned throughout the course and demonstrate your ability to manage scalable AI systems in a production environment.

## Instructions

1. Deploy the pre-trained model to Google AI Platform.
2. Set up Google Cloud Monitoring to track the deployed model’s performance.
3. Configure auto-scaling for the deployed model.

## Solution Code

_Note: Run `test.py` to test your code._

```python
from google.cloud import aiplatform
from google.cloud import monitoring_v3
from google.api_core.operation import Operation

# Step 1: Deploy the pre-trained model to Google AI Platform
aiplatform.init(_____)
model = _____
endpoint = model.deploy(_____)
# Step 2: Set up Google Cloud Monitoring to track the deployed model's performance
client = _____
project_name = _____
descriptor = _____
# Step 3: Configure auto-scaling for the deployed model
autoscaling_policy = _____
operation = _____
