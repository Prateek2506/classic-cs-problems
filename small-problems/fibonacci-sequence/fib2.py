count = 0


def fib2(n: int) -> int:
    global count
    count = count + 1
    if n < 2:
        return n
    return fib2(n-1) + fib2(n-2)


print(fib2(20))
print('number of calls = ', count)
