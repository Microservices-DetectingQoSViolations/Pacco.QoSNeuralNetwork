from datetime import datetime

from src.kube.constants import pod_jobs
from src.kube.pod import get_pods
from src.prometheus.time_utils import generate_time
from src.prometheus.metrics import metric_labels
from src.prometheus.constants import prometheus_endpoint

import tensorflow_io as tfio

offset = 1597501140
offset_in_ms = offset * 1000
data_length = 210

pods_data = get_pods()

dataset = tfio.experimental.IODataset.from_prometheus('rate(application_qos_violation[5s])', data_length,
                                                      offset=offset_in_ms, endpoint=prometheus_endpoint)

print("Dataset Spec:\n{}\n".format(dataset.element_spec))

for (timestamp, value) in dataset:
    # time is milli second, convert to data time:
    timestamp = timestamp // 1000
    time = datetime.fromtimestamp(timestamp)
    print("{} {}: {}".format(timestamp, time, value[pod_jobs]['10.1.39.142:80']['']))