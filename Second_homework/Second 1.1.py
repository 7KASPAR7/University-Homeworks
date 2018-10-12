from unittest import TestCase, main
import time
from memory_profiler import profile

@profile
def factorial(n):
    if n<0 or n!=n//1:
       F='Факториал определен только для целых неотрицательных чисел'
    else:
        F=1
        for i in range(1,n+1):
            F=F*i
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
start_time = time.time(factorial(8))
main()
print("--- %s seconds ---" % (time.time(factorial(8)) - start_time))