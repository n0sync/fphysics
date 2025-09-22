import unittest

class TestKinematics(unittest.TestCase):
    
    def test_position_calculation(self):
        initial_position = 0
        velocity = 10
        time = 5
        expected_position = initial_position + velocity * time
        self.assertEqual(expected_position, 50)
    
    def test_velocity_calculation(self):
        initial_velocity = 0
        acceleration = 9.8
        time = 2
        expected_velocity = initial_velocity + acceleration * time
        self.assertAlmostEqual(expected_velocity, 19.6)

if __name__ == '__main__':
    unittest.main()

