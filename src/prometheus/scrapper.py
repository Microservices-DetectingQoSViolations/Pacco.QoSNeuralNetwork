from datetime import datetime

import tensorflow_io as tfio

dataset = tfio.experimental.IODataset.from_prometheus(
      "application_qos_violation", 210, offset=1597501140000, endpoint="http://localhost:9090")

print("Dataset Spec:\n{}\n".format(dataset.element_spec))

for (timestamp, value) in dataset:
    # time is milli second, convert to data time:
    timestamp = timestamp // 1000
    time = datetime.fromtimestamp(timestamp)
    print("{} {}: {}".format(timestamp, time, value['kubernetes-pods']['10.1.39.142:80']['application_qos_violation']))