from src.kube.pod import get_pod_names
from src.prometheus.time_utils import generate_time
from src.prometheus.metrics import metric_labels
from src.prometheus.constants import prometheus_endpoint, prometheus_query, excluding_services

import pandas as pd
import requests

data_length = 420
offsets = [1597954309, 1597954909, 1597955510, 1597956110, 1597956710,
           1597957310, 1597957910, 1597958510, 1597959110, 1597959710,
           1597960310, 1597960910, 1597961510, 1597962111, 1597962711,
           1597963311, 1597963912, 1597964512, 1597965112, 1597965712,
           1597966312, 1597966912]

offsets_in_ms = [((offset - data_length + 1), offset) for offset in offsets]

pods = ['vehicles-service', 'identity-service', 'customers-service', 'deliveries-service', 'orders-service',
        'availability-service', 'parcels-service', 'pricing-service'] #get_pod_names(excluding_services)

datasets = []

for offset in offsets_in_ms:
    prom_data_by_pods = {}
    for job_name in metric_labels:
        for metric in metric_labels[job_name]:
            response =requests.get(prometheus_endpoint + prometheus_query,
                                   params={'query': metric[1], 'start': offset[0], 'end': offset[1], 'step':1})
            prometheus_data = response.json()['data']['result']

            for pod in pods:
                metric_data = next(data['values'] for data in prometheus_data if data['metric']['app'] == pod)
                metric_data = map(lambda val: float(val[1]), metric_data)
                prom_data_by_pods[metric[0] + '_' + pod] = metric_data
    datasets.append(pd.DataFrame.from_dict(prom_data_by_pods))