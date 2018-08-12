import os
from time import sleep

for i in range(1,100):
    os.system("java -cp bin\;lib\* BenchmarkNumerosPrimos "+str(i)+" 80000")
    sleep(2)
