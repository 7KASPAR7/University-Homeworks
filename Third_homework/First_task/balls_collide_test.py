from balls_collide import balls_collide
from unittest import TestCase, main


class PerfectTest(TestCase):
    def test_true_values(self):
        self.assertTrue(balls_collide((6, 1, 4), (4, 1, 5)))
        self.assertTrue(balls_collide((0, 1, 4.8), (0, 1, 4.8)))
        self.assertTrue(balls_collide((5, 5, 5), (5, 5, 5)))
        self.assertTrue(balls_collide((0, 0, 5.5), (5.5, 0, 5.5)))

    def test_false_values(self):
        self.assertFalse(balls_collide((3, 1, 8.7), (4, 2, 3)))
        self.assertFalse(balls_collide((5, 2, 2.4), (1, 2, 1)))

    def test_Raises(self):
        self.assertRaises(ValueError, balls_collide, (3.9, 1, -3), (2, 5, 6))
        self.assertRaises(ValueError, balls_collide, (0, 0, 6), (7, 51, -10))


main()
