from unittest import TestCase, main
from poly_logic import program


class PerfectTest(TestCase):
    def test_values(self):
        self.assertEqual(program('12X^4-23X^2+123x-12'), '48x^3-46x+123')
        self.assertEqual(program('X^7-25X^3+13x-12'), '7x^6-75x^2+13')
        self.assertEqual(program('-6*X^2-10*X^5+x-12'), '-12x-50x^4+1')
        self.assertEqual(program('62X^3'), '186x^2')
        self.assertEqual(program('123456789'), '0')
        self.assertEqual(program('-50X^6'), '-300x^5')


main()
