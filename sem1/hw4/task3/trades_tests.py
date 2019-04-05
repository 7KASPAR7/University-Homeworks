from unittest import TestCase, main
from trades_logic import begin,  find_birge, share

arg1 = ['100000009'], [13514], [100], ['V']
arg = [[0, 1, 13514.0, 'V']]


class PerfectTest(TestCase):
    def test_values(self):
        self.assertEqual(begin('trades1.csv'), (arg1))
        self.assertEqual(begin('trades2.csv'), ([], [], [], []))
        self.assertEqual(find_birge('V'), ('V', {'V': 0}))
        self.assertEqual(find_birge(''), ('', {}))
        self.assertEqual(share(['100000009'], [13514], [100], ['V'], 'V'), arg)
        self.assertEqual(share([], [], [], [], ''), ([]))


main()
