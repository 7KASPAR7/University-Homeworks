from unittest import TestCase, main

def factorial(n):
    if type(n) != int:
        raise TypeError('Некорректный ввод данных')
    elif n < 0:
        raise ValueError('Факториал определен только для положительных чисел')
    else:
        F=1
        for i in range(1,n+1):
            F=F*i
    return F

def Pascal(n):
    if type(n)!=int:
        raise TypeError('Некорректный ввод данных')
    elif n <= 0:
        raise ValueError('Факториал определен только для положительных чисел')
    else:
        RESULT=[[1]]
        for i in range(1,n):
            result=[]
            for l in range(0,i+1):
                a=factorial(i)/(factorial(l)*factorial(i-l))
                a=int(a)
                result.append(a)
            RESULT.append(result)
        return RESULT

class PerfectTest(TestCase):
    def test_valid_values(self):
        self.assertEqual(Pascal(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])
        self.assertEqual(Pascal(1), [[1]])
    def test_Errors(self):
        self.assertRaises(ValueError, Pascal, 0)
        self.assertRaises(ValueError, Pascal, -6)
        self.assertRaises(TypeError, Pascal, -2.5)
        self.assertRaises(TypeError, Pascal, 8.5)
        self.assertRaises(TypeError, Pascal, 'sss')
        self.assertRaises(TypeError, Pascal, [])

main()