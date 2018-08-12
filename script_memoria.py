import os
from time import sleep

def exp(kb):
    os.system("java -cp bin/;lib/* BenchmarkAcessoMemoria "+str(kb)+" 80000000")
    sleep(10)
    exp(kb*2)

exp(1048576)


    
    
