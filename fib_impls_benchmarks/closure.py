#! Автор кода: https://m.habr.com/ru/users/Doublesharp/
# Из его статьи про рекурсию в питоне я и взял это

import time

start_time = time.perf_counter()

def main():
    def fib():
        x1, x2 = 0, 1
        def get_next():
            nonlocal x1, x2
            x3 = x1 + x2
            x1, x2 = x2, x3
            return x3
        return get_next
    
    def fib_closure(n):
        f = fib()
        for i in range(2, n+1):
            num = f()
        return num

    print(fib_closure(20))

main()
print((time.perf_counter() - start_time) / 1000)
