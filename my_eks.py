from kubernetes import client, config

# Load kubeconfig
config.load_kube_config()

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
                    image="your-image-name",  # Replace with your Docker image
                    ports=[client.V1ContainerPort(container_port=5000)],
                )
            ]),
        ),
    ),
)

namespace = 'default'  # Change to your namespace
deployment_name = 'flask-app'

try:
    # Check if the deployment already exists
    existing_deployment = api_instance.read_namespaced_deployment(deployment_name, namespace)
    print(f"Deployment '{deployment_name}' already exists.")
except client.exceptions.ApiException as e:
    if e.status == 404:
        # Deployment does not exist, safe to create
        api_instance.create_namespaced_deployment(namespace, deployment)
        print(f"Deployment '{deployment_name}' created.")
    else:
        print(f"Error occurred: {e}")

