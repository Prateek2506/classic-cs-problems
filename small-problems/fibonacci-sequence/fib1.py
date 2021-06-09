def fib1(n: int) -> int:
    return fib1(n-1) + fib1(n-2)
print(fib1(5))