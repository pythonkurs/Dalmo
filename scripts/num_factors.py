import time
import os
import multiprocessing
from collections import Counter
import IPython.parallel
from IPython.parallel import Client
from Dalmo.session7 import factorize as fact1

cli = Client()
dview = cli[:]

@dview.parallel(block=True)
def get_factorize_in_ipython_parallell(num_factors):
    import time
    from Dalmo.session7 import factorize as fact2
    start_time=time.time()
    Fact=[]
    for i in num_factors:
        Fact.append(fact2(i))
    return time.time()-start_time, Fact, num_factors

def get_factorize_in_serial(num_factors):
    start_time=time.time()
    Fact=[]
    for i in num_factors:
        Fact.append(fact1(i))
    return time.time()-start_time, Fact, num_factors

def get_factorize_in_parallell(num_factors):
    start_time=time.time()
    pool = multiprocessing.Pool()
    L = pool.map_async(fact1, num_factors)
    Fact = L.get()
    return time.time()-start_time, Fact, num_factors

    
if __name__ == "__main__":
    num_factors=range(2,10)
    Num_Unique_Factors1 = []
    Num_Unique_Factors2 = []
    Num_Unique_Factors3 = []
    
    Serial = get_factorize_in_serial(num_factors)
    Parallel = get_factorize_in_parallell(num_factors)
    Parallel_IP = get_factorize_in_ipython_parallell(num_factors)
    
    for i in Serial[1]:
        Num_Unique_Factors1.append(len(Counter(i)))
    
    for i in Parallel[1]:
        Num_Unique_Factors2.append(len(Counter(i)))

    """for i in Parallel_IP[1]:
        Num_Unique_Factors3.append(len(Counter(i)))"""

    Unique1 = dict(Counter(Num_Unique_Factors1))
    Unique2 = dict(Counter(Num_Unique_Factors2))
    "Unique3 = dict(Counter(Num_Unique_Factors3))"
    
    print Serial
    print Parallel
    print Parallel_IP
    
    """print Serial[0], Serial[1], Unique1
    
    print Parallel[0], Parallel[1], Unique2

    print Parallel_IP[0], Parallel_IP[1], Unique3"""
