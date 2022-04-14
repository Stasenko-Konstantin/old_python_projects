import time

start_time = time.perf_counter()

def main():
    def fib_rec(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return fib_rec(n-1) + fib_rec(n-2)

    print(fib_rec(20))

main()
print((time.perf_counter() - start_time) / 1000)
