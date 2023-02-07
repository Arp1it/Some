import time
from functools import lru_cache

m = int(input("enter: \n"))

@lru_cache(maxsize = m)
def some_time(n):
    time.sleep(n)
    return n

if __name__ == "__main__":
    print("hi")
    some_time(6)
    print("hello")
    some_time(6)
    print("bye")
    some_time(7)
    print("bye")