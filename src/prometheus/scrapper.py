from datetime import datetime

import tensorflow_io as tfio

dataset = tfio.experimental.IODataset.from_prometheus(
      "application_qos_violation", 210, offset=1597501140000, endpoint="http://localhost:9090")

print("Dataset Spec:\n{}\n".format(dataset.element_spec))

for (time, value) in dataset:
    # time is milli second, convert to data time:
    time = datetime.fromtimestamp(time // 1000)
    print("{}: {}".format(time, value['kubernetes-pods']['10.1.39.142:80']['application_qos_violation']))