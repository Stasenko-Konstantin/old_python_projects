import time

start_time = time.perf_counter()

def main():
    def fib_tail_rec(n):
        def help(acc, curr, count):
            if count == n:
                return acc
            else:
                return help(acc+curr, acc, count+1)
        return help(1, 0, 1)

    print(fib_tail_rec(20))

main()
print((time.perf_counter() - start_time) / 1000)
