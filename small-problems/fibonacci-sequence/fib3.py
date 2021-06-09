# memoization approach
from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}
callsTofib3 = 0


def fib3(n: int) -> int:
    global callsTofib3
    callsTofib3 = callsTofib3+1
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2)
    return memo[n]


if __name__ == "__main__":
    print(fib3(20))
    print('Number of calls = ', callsTofib3)
