from time import sleep
from dask import compute, delayed
import dask.multiprocessing
from dask.distributed import Client

@delayed
def is_prime(n):
    i = 0
    while i < 1000000:  # Uma espera processada so pra 
                        # gente se achar importante
        i += 1
    for j in range(2, n - 1):
        if (n % j) == 0:
            print('%s no' % n)
            return False
    print('%s yes' % n)
    return True

@delayed
def Print(arr):
    print(arr)


primes100 = [is_prime(n) for n in range(2, 101)]
t = Print(primes100)

# results = compute(t, get=dask.multiprocessing.get)

client = Client('localhost:8786')
results = compute(t, get=client.get)
