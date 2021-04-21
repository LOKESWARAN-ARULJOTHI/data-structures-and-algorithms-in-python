# caching the old values 
fib_cache={}

def fib(n):
    if n in fib_cache:
        return fib_cache[n]

    if n<=1:
        return 1
    else:
        value = fib(n-1)+ fib(n-2)
        fib_cache[n]=value
        return value
print('Fibonacci value of 998:',fib(998))
