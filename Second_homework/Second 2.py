from unittest import TestCase, main

def perfect(a):
    result = []
    if a!=a//1:
        raise ValueError('Требуется целое число')
    elif a<=0:
        raise ValueError('Требуется неотрицательное число')
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

class PerfectTest(TestCase):
    def test_valid_values(self):
        self.assertTrue(perfect(6))
        self.assertTrue(perfect(28))
        self.assertTrue(perfect(8128))
        self.assertFalse(perfect(1))
        self.assertFalse(perfect(8))
        self.assertRaises(ValueError, perfect, 8.3)
        self.assertRaises(ValueError, perfect, -2.4)
        self.assertRaises(ValueError, perfect, 0)
        self.assertRaises(ValueError, perfect, -6)
        self.assertRaises(ValueError, perfect, -25)
main()