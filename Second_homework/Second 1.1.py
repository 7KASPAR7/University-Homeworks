from unittest import TestCase, main
import time
from memory_profiler import profile


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
@profile
def timer(n):
    factorial(n)
start_time=time.time()
timer(800)
print('time:',time.time()-start_time)
class PerfectTest(TestCase):
    def test_valid_values(self):
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
    def test_Errors(self):
        self.assertRaises( ValueError, factorial, -6)
        self.assertRaises(TypeError, factorial, -2.5)
        self.assertRaises(TypeError, factorial, 8.5)
        self.assertRaises(TypeError, factorial, 'dd')
        self.assertRaises( TypeError, factorial, [])

main()
