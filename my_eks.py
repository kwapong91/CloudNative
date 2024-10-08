from kubernetes import client, config

# Load kubeconfig
config.load_kube_config()

api_client = client.ApiClient()

# Create an instance of the API
api_instance = client.AppsV1Api()

# Define your deployment (example configuration)
deployment = client.V1Deployment(
    api_version="apps/v1",
    kind="Deployment",
    metadata=client.V1ObjectMeta(name="flask-app"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector={'matchLabels': {'app': 'flask-app'}},
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels={'app': 'flask-app'}),
            spec=client.V1PodSpec(containers=[
                client.V1Container(
                    name="flask-container",
                    image="235494808933.dkr.ecr.us-east-1.amazonaws.com/cloudnative-app",  # Replace with your Docker image
                    ports=[client.V1ContainerPort(container_port=5002)],
                )
            ]),
        ),
    ),
)

namespace = "default"
deployment_name = "flask-app"


api_instance = client.AppsV1Api(api_client)
api_instance.patch_namespaced_deployment(
    name=deployment_name,
    namespace=namespace,
    body=deployment

)

