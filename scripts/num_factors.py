import time
import os
import multiprocessing
from collections import Counter
import IPython.parallel
from IPython.parallel import Client
from Dalmo.session7 import factorize
import argparse

cli = Client()
dview = cli[:]

@dview.parallel(block=True)
def get_factorize_in_ipython_parallell(num_factors):
    from Dalmo.session7 import factorize
    Fact = []
    for i in num_factors:
        Fact.append(factorize(i))
    return Fact

def get_factorize_in_serial(num_factors):
    start_time=time.time()
    Fact = []
    for i in num_factors:
        Fact.append(factorize(i))
    return Fact, time.time()-start_time

def get_factorize_in_parallell(num_factors):
    start_time=time.time()
    pool = multiprocessing.Pool()
    L = pool.map_async(factorize, num_factors)
    Fact = L.get()
    return Fact, time.time()-start_time

def main():
    parser = argparse.ArgumentParser(description="A script to check different way of processing data, serial, multiprocessing and IPython Parallel")
    parser.add_argument('-s', '--serial', action="store_true", dest="serial", default=False
                         ,help="Chose a way to process the data")
    parser.add_argument('-m', '--multiprocessing', action="store_true", dest="multi", default=False
                        ,help="Chose a way to process the data")
    parser.add_argument('-i', '--ipython', action="store_true", dest="ipython", default=False
                        ,help="Chose a way to process the data")
    args = parser.parse_args()

    num_factors=range(2,500000)
    Num_Unique_Factors1 = []
    Num_Unique_Factors2 = []
    Num_Unique_Factors3 = []
    
    if args.serial:
        Serial = get_factorize_in_serial(num_factors)
        for i in Serial[0]:
            Num_Unique_Factors1.append(len(Counter(i)))
        Unique1 = dict(Counter(Num_Unique_Factors1))
        print Serial[1], "seconds with serial", Unique1

    if args.multi:
        Parallel = get_factorize_in_parallell(num_factors)
        for i in Parallel[0]:
            Num_Unique_Factors2.append(len(Counter(i)))
        Unique2 = dict(Counter(Num_Unique_Factors2))
        print Parallel[1], "seconds with multiprocessing", Unique2


    if args.ipython:
        start_time_IP = time.time()
        Parallel_IP = get_factorize_in_ipython_parallell(num_factors)
        Parallel_IP_time = time.time() - start_time_IP
        for i in Parallel_IP:
            Num_Unique_Factors3.append(len(Counter(i)))
        Unique3 = dict(Counter(Num_Unique_Factors3))
        print Parallel_IP_time, "seconds with IPython Parallel ", Unique3

if __name__ == "__main__":
    main()