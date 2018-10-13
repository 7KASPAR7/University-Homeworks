from unittest import TestCase, main

def factorial(n):
    if n<0 or n!=n//1:
        raise ValueError('Факториал определен только для целых неотрицательных чисел')
    else:
        F=1
        for i in range(1,n+1):
            F=F*i
    return F

def Pascal(n):
    if n<=0 or n//1!=n:
        return 'Некорректный ввод данных'
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
Pascal(6)


class PerfectTest(TestCase):
    def test_valid_values(self):
        self.assertEqual(Pascal(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])
        self.assertEqual(Pascal(1), [[1]])
        self.assertEqual(Pascal(0), 'Некорректный ввод данных')
        self.assertRaises(ValueError, factorial, -6)
        self.assertRaises(ValueError, factorial, -2.5)
        self.assertRaises(ValueError, factorial, 8.5)

main()