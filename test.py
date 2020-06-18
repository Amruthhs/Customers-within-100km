import unittest
from CustomerRecords_Great_Circle import CustomerRecords


class TestCustomerRecords(unittest.TestCase):
    """Unit tests for the CustomerRecords class"""

    def test_get_distance_method(self):
        """Assert that the distance between hq and the first entry in Customer_list.txt is 50000 meters"""

        test = CustomerRecords('Customer_list.txt', 100000, 53.339428, -6.257664)
        self.assertLess(test.get_distance(
            53.339428, -6.257664, 52.986375, -6.043701), 50000)
        
    def test_read_file(self):
        """Assert that there are 16 correct answers in Customer_list.txt"""

        test = CustomerRecords('Customer_list.txt', 100000, 53.339428, -6.257664)
        self.assertEqual(len(test.read_file()), 16)

    def test_measure_distance_method(self):
        """Comparing the distance between hq and the entry in customer_list.txt"""

        test = CustomerRecords('Customer_list.txt', 100000, 53.339428, -6.257664)
        self.assertGreater(test.get_distance(
            53.339428, -6.257664, 51.515314, -0.155163), 460)

if __name__ == '__main__':
    unittest.main()