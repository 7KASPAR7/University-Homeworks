from unittest import TestCase, main

def perfect(a):
    result = []
    if a!=a//1:
        result='Требуется целое число'
    elif a<=0:
        result='Требуется неотрицательное число'
    else:
        S=0
        for i in range(1,a):
             if a%i==0:
                 S=S+i
        if a==S:
             result=True
        else:
             result=False
    return result
print(perfect(8128))

class PerfectTest(TestCase):
    def test_valid_values(self):
        self.assertTrue(perfect(6))
        self.assertEqual(perfect(0),'Требуется неотрицательное число')
        self.assertFalse(perfect(1))
        self.assertEqual(perfect(-6),'Требуется неотрицательное число')
        self.assertEqual(perfect(-25),'Требуется неотрицательное число')
        self.assertTrue(perfect(28))
        self.assertTrue(perfect(8128))
        self.assertFalse(perfect(8))
        self.assertEqual(perfect(8.3), 'Требуется целое число')
        self.assertEqual(perfect(-2.4), 'Требуется целое число')
main()