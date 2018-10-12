from unittest import TestCase, main
import time
from memory_profiler import profile
@profile
def factorial(n):
    if n<0 or n!=n//1:
       F='Факториал определен только для целых неотрицательных чисел'
    else:
        if n==0:
            F=1
        else:
            F=factorial(n-1)*n
    return F
start_time=time.time()
print(factorial(8))
print(time.time()-start_time)
class PerfectTest(TestCase):
    def test_valid_values(self):
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(-6), 'Факториал определен только для целых неотрицательных чисел')
        self.assertEqual(factorial(-2.5), 'Факториал определен только для целых неотрицательных чисел')
        self.assertEqual(factorial(8.5), 'Факториал определен только для целых неотрицательных чисел')

main()
