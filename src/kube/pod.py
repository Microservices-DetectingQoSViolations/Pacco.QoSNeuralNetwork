from kubernetes import client, config


def get_pods():
    config.load_kube_config()

    v1 = client.CoreV1Api()
    print("Getting pods with their IPs:")
    pods = v1.list_pod_for_all_namespaces(watch=False)

    return [(pod.status.pod_ip + ':80', pod.metadata.labels['app'])
            for pod in pods.items if 'app' in pod.metadata.labels and 'service' in pod.metadata.labels['app']]

def get_pod_names(excluding_names):
    config.load_kube_config()

    v1 = client.CoreV1Api()
    print("Getting Pod names:")
    pods = v1.list_pod_for_all_namespaces(watch=False)

    return list(set(pod.metadata.labels['app']
            for pod in pods.items if 'app' in pod.metadata.labels
            and 'service' in pod.metadata.labels['app']
            and pod.metadata.labels['app'] not in excluding_names))
