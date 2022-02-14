from random import random
import threading
from time import time


class Contador():
    def __init__(self,conta = 0):
        self.loked = threading.Lock()
        self.conta_send = conta

    def incrementar(self): #this -> self
        self.loked.acquire() #Espera a que loked termine
        try:
            self.conta_send += 1
            print(self.conta_send)
        finally:
            self.loked.release()
def func_conta(x):
    for y in range(2):
        time_f = random.random()
        time.sleep(time_f)
        # print(y)
if __name__ == " _main_ ":
    Contador = Contador()
    for y in range(2):
        tsart =threading.Thread(target=func_conta, args=(Contador,))
        tsart.start()