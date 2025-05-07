'''
Write a Python function `fibonacci(n: int) -> int` that returns the nth number in the Fibonacci sequence,
where `n` is a non-negative integer.
Example:
fibonacci(0) 0
fibonacci(1) 1
fibonacci(6) 8 (The sequence is 0, 1, 1, 2, 3, 5, 8, 13...)
'''
def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a,b = b, a+b
        
fibo(10)