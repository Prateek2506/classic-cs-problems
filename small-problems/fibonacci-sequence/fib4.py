from functools import lru_cache
count = 0

# automatic memoization


@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    global count
    count = count + 1
    if n < 2:
        return n
    return fib4(n-1) + fib4(n-2)


print(fib4(20))
print('number of calls = ', count)
