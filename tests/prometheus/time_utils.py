import unittest
from src.prometheus.time_utils import generate_time

class TestGenerateTime(unittest.TestCase):
    def test_valid_date(self):
        generated_data = generate_time(1597501140, 210)

        self.assertEqual(1597500930, generated_data[0])
        self.assertEqual(1597501139, generated_data[-1])
        self.assertNotIn(1597501140, generated_data)

if __name__ == '__main__':
    unittest.main()