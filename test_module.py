import unittest
from mean_var_std import calculate

class TestCalculate(unittest.TestCase):
    
    def test_calculate_with_valid_input(self):
        """Test calculate function with valid 9-element list"""
        result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
        
        self.assertEqual(result['mean'], [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0])
        self.assertEqual(result['variance'], [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667])
        self.assertEqual(result['standard deviation'], [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611])
        self.assertEqual(result['max'], [[6, 7, 8], [2, 5, 8], 8])
        self.assertEqual(result['min'], [[0, 1, 2], [0, 3, 6], 0])
        self.assertEqual(result['sum'], [[9, 12, 15], [3, 12, 21], 36])
    
    def test_calculate_raises_error_with_less_than_9_elements(self):
        """Test that ValueError is raised with less than 9 elements"""
        with self.assertRaises(ValueError) as context:
            calculate([1, 2, 3, 4, 5])
        
        self.assertEqual(str(context.exception), "List must contain nine numbers.")
    
    def test_calculate_raises_error_with_more_than_9_elements(self):
        """Test that ValueError is raised with more than 9 elements"""
        with self.assertRaises(ValueError) as context:
            calculate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        
        self.assertEqual(str(context.exception), "List must contain nine numbers.")
    
    def test_calculate_returns_lists_not_arrays(self):
        """Test that returned values are lists, not numpy arrays"""
        result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
        
        for key in result:
            self.assertIsInstance(result[key], list)
            for item in result[key]:
                if isinstance(item, list):
                    for val in item:
                        self.assertNotIsInstance(val, type(None))

if __name__ == '__main__':
    unittest.main()
