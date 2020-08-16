import unittest
from src.prometheus.metrics_excluder import exclude_metrics_by_service_name

class TestMetricsExcluder(unittest.TestCase):
    def test_empty(self):
        generated_data = exclude_metrics_by_service_name([], True)

        self.assertEqual('', generated_data)

        generated_data = exclude_metrics_by_service_name([], False)

        self.assertEqual('', generated_data)

    def test_one_service(self):
        generated_data = exclude_metrics_by_service_name(['api-gateway-service'], True)

        self.assertEqual('''{app!~"api-gateway-service"}''', generated_data)

        generated_data = exclude_metrics_by_service_name(['api-gateway-service'], False)

        self.assertEqual('''app!~"api-gateway-service", ''', generated_data)

    def test_many_services(self):
        generated_data = exclude_metrics_by_service_name(['api-gateway-service', 'order-maker-service'], True)

        self.assertEqual('''{app!~"api-gateway-service|order-maker-service"}''', generated_data)

        generated_data = exclude_metrics_by_service_name(['api-gateway-service', 'order-maker-service'], False)

        self.assertEqual('''app!~"api-gateway-service|order-maker-service", ''', generated_data)

if __name__ == '__main__':
    unittest.main()