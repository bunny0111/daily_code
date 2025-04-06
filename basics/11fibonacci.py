'''
print fibonacci series to n numbers.
'''
def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a+b
    print()
    
fibo(10)