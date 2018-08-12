import os
from time import sleep

def primos_thread():
    for i in range(1,20000,10):
        thread = str(i)
        os.system("java -cp bin\;lib\* BenchmarkNumerosPrimos "+thread+" 80000")
        sleep(2)

def primos_array():
    for i in range(440000,100000000,100000):
        array = str(i)
        os.system("java -cp bin\;lib\* BenchmarkNumerosPrimos 100 "+array)
        sleep(2)

primos_array()
