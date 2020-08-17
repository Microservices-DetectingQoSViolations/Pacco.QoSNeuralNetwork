from datetime import datetime
from time import time
import math

from src.kube.pod import get_pod_names
from src.prometheus.time_utils import generate_time
from src.prometheus.metrics import metric_labels
from src.prometheus.constants import prometheus_endpoint, excluding_services

import tensorflow as tf
import tensorflow_io as tfio

offset = 1597501140
offset_in_ms = offset * 1000
data_length = 210

pods = get_pod_names(excluding_services)

datasets = []

time_series = generate_time(offset, data_length)


for job_name in metric_labels:
    for metric in metric_labels[job_name]:
        print(f'Download {metric} from prometheus')
        dataset_prom = tfio.experimental.IODataset.from_prometheus(metric[1], data_length, offset=offset_in_ms, endpoint=prometheus_endpoint)
        for pod in pods:
            dataset = dataset_prom.map(lambda k, v: (k // 1000, v[str(job_name)][pod]['']))

            dataset_list = list(dataset.as_numpy_iterator())
            if (len(dataset_list) != len(time_series)):
                last = dataset_list[0][1]
                for idx, value in enumerate(time_series):
                    try:
                        dest_elem = dataset_list[idx]
                    except:
                        dataset_list.append((value, last))
                        continue
                    if math.isnan(dest_elem[1]):
                        dataset_list[idx] = last
                    if dest_elem[0] != value:
                        dataset_list[idx:idx] = [(value, last)]
                    last = dataset_list[idx][1]
                dataset = tf.data.Dataset.from_tensor_slices([x[1] for x in dataset_list])

            # find the max value and scale the value to [0, 1]
            v_max = dataset.reduce(tf.constant(0.0, tf.float64), tf.math.maximum)
            dataset = dataset.map(lambda _, v: (v / v_max))
            datasets.append(dataset)
print(datasets)