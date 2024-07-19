import boto3
from google.cloud import aiplatform
from google.cloud import monitoring_v3
from google.api_core.exceptions import GoogleAPIError
import requests

def test_step_1_deploy_model():
    try:
        aiplatform.init(project='your-project-id')

        model = aiplatform.Model('projects/your-project-id/locations/us-central1/models/your-model-id')
        endpoint = model.deploy(
            deployed_model_display_name='my-deployed-model',
            machine_type='n1-standard-4',  
            min_replica_count=1,
            max_replica_count=5, 
            traffic_split={"0": 100}
        )
        print(f"Step 1: Endpoint deployed successfully: {endpoint.resource_name}")
    except GoogleAPIError as e:
        print(f"Step 1: Failed to deploy endpoint. Error: {e}")

def test_step_2_set_up_monitoring():
    try:
        client = monitoring_v3.MetricServiceClient()
        project_name = f"projects/your-project-id"

        # Create a metric descriptor for monitoring
        descriptor = monitoring_v3.MetricDescriptor()
        descriptor.type = "custom.googleapis.com/deployed_model/latency"
        descriptor.metric_kind = monitoring_v3.MetricDescriptor.MetricKind.GAUGE
        descriptor.value_type = monitoring_v3.MetricDescriptor.ValueType.DOUBLE
        descriptor.description = "The latency of the deployed model"

        client.create_metric_descriptor(name=project_name, metric_descriptor=descriptor)
        print("Step 2: Metric descriptor created successfully")
    except GoogleAPIError as e:
        print(f"Step 2: Failed to create metric descriptor. Error: {e}")

def test_step_3_configure_auto_scaling():
    try:
        aiplatform.init(project='your-project-id')
        endpoint = aiplatform.Endpoint('projects/your-project-id/locations/us-central1/endpoints/your-endpoint-id')

        # Get the current auto-scaling policy for the endpoint
        autoscaling_policy = endpoint.get_traffic_split()
        print(f"Current auto-scaling policy: {autoscaling_policy}")

        # Update auto-scaling configuration if necessary
        if autoscaling_policy["0"] != 100:
            autoscaling_policy["0"] = 100
            endpoint.update_traffic_split(autoscaling_policy)
            print(f"Updated auto-scaling policy: {autoscaling_policy}")

        # Ensure the endpoint is configured for auto-scaling
        operation = aiplatform.Endpoint.deploy(
            endpoint_name=endpoint.resource_name,
            deployed_model_display_name='my-deployed-model',
            machine_type='n1-standard-4',
            min_replica_count=1,
            max_replica_count=5
        )
        operation.result()
        print(f"Step 3: Auto-scaling configured successfully: min_replica_count=1, max_replica_count=5")
    except GoogleAPIError as e:
        print(f"Step 3: Failed to configure auto-scaling. Error: {e}")

if __name__ == "__main__":
    print("Testing Step 1: Deploy Model to Google AI Platform")
    test_step_1_deploy_model()
    
    print("Testing Step 2: Set Up Google Cloud Monitoring")
    test_step_2_set_up_monitoring()
    
    print("Testing Step 3: Configure Auto-Scaling for the Deployed Model")
    test_step_3_configure_auto_scaling()
