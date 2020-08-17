import unittest
import tensorflow as tf
import math

class TestTensorflowDatasetOperations(unittest.TestCase):
    def test_join_dataset_with_constant(self):
        a = tf.data.Dataset.range(1, 4)
        b = tf.data.Dataset.from_tensors(tf.constant(4, dtype='int64'))
        c = tf.data.Dataset.range(5, 6)

        d = a.concatenate(b).concatenate(c)

        a_length = len(list(a.as_numpy_iterator()))
        b_length = len(list(b.as_numpy_iterator()))
        c_length = len(list(c.as_numpy_iterator()))
        d_length = len(list(d.as_numpy_iterator()))

        self.assertEqual(a_length + b_length + c_length, d_length)


    def test_fill_no_data(self):
        source_dataset = enumerate(tf.data.Dataset.range(1,5))

        sp = enumerate(list(range(1,5)))
        dest_dataset_x = tf.data.Dataset.from_tensor_slices([1,3])
        dest_dataset_y = tf.data.Dataset.from_tensor_slices([0, 5])

        dest_dataset = tf.data.Dataset.zip((dest_dataset_x, dest_dataset_y))
        dest_list = list(tf.data.Dataset.zip((dest_dataset_x, dest_dataset_y)).as_numpy_iterator())

        last = dest_list[0][1]

        for idx, value in sp:
            try:
                dest_elem = dest_list[idx]
            except:
                dest_list.append((value, last))
                continue
            if math.isnan(dest_elem[1]):
                dest_list[idx] = last
            if dest_elem[0] != value:
                dest_list[idx:idx] = [(value, last)]
            last = dest_list[idx][1]

        self.assertEqual([(1, 0), (2, 0), (3, 5), (4, 5)], dest_list)

if __name__ == '__main__':
    unittest.main()