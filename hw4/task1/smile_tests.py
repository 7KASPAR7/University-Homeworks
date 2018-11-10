from unittest import TestCase, main
from smile_logic import program


class PerfectTest(TestCase):
    def test_true_values(self):
        self.assertTrue(program('{Hello[]}'))
        self.assertTrue(program('[({(Hi)})]'))
        self.assertTrue(program('{}[](){[(())]}'))
        self.assertTrue(program('{{{([([([1234321])])])}}}'))
        self.assertTrue(program('Без скобок!'))

    def test_false_values(self):
        self.assertFalse(program('{Hello[}'))
        self.assertFalse(program('{Hi]'))
        self.assertFalse(program('{{{9900[))}'))
        self.assertFalse(program('{{}[qqqq]}(()'))


main()
