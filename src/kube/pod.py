from kubernetes import client, config


def get_pods():
    config.load_kube_config()

    v1 = client.CoreV1Api()
    print("Getting pods with their IPs:")
    return v1.list_pod_for_all_namespaces(watch=False)


def list_pods():
    pods = get_pods()
    for pod in pods.items:
        print("%s\t%s\t%s" % (pod.status.pod_ip, pod.metadata.namespace, pod.metadata.name))