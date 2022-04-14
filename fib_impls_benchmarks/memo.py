import time

start_time = time.perf_counter()

def main():
    def fib_memo(n):
        memo = {0: 0, 1: 1}
        def help(x):
            if x not in memo:
                memo[x] = fib_memo(x-1) + fib_memo(x-2)
            return memo[x]
        return help(n)

    print(fib_memo(20))

main()
print((time.perf_counter() - start_time) / 1000)
