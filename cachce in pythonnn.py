import time
from functools import lru_cache

@lru_cache(maxsize = 1)
def some(n):
    time.sleep(n)
    return n

if __name__ == "__main__":

    print("Now processing")
    some(3)
    some(1)
    some(4)
    some(2)
    print("Dialling....")
    # input()
    some(3)
    print("calling again")