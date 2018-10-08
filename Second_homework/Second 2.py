from unittest import TestCase, main

def perfect(a):
    result = []
    if a!=a//1:
        result='Требуется целое число'
    elif a<=0:
        result='Несовершенное число'
    else:
        S=0
        for i in range(1,a):
             if a%i==0:
                 S=S+i
        if a==S:
             result='Совершенное число'
        else:
             result='Несовершенное число'
    return result
print(perfect(8128))

class PerfectTest(TestCase):
    def test_valid_values(self):
        self.assertEqual(perfect(6), 'Совершенное число')
        self.assertEqual(perfect(0), 'Несовершенное число')
        self.assertEqual(perfect(1), 'Несовершенное число')
        self.assertEqual(perfect(-6), 'Несовершенное число')
        self.assertEqual(perfect(-25), 'Несовершенное число')
        self.assertEqual(perfect(28), 'Совершенное число')
        self.assertEqual(perfect(8128), 'Совершенное число')
        self.assertEqual(perfect(8), 'Несовершенное число')
        self.assertEqual(perfect(8.3), 'Требуется целое число')
        self.assertEqual(perfect(-2.4), 'Требуется целое число')
main()