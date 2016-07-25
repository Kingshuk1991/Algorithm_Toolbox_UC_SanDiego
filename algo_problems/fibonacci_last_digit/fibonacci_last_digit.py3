# Uses python3
import sys

def get_fibonacci_last_digit(n):
    f=[0,1]+[None]*(n-1)
    for i in range(2,n+1):
        f[i]=(f[i-1]+f[i-2])%10
    return f[n]

n = int(input())
print(get_fibonacci_last_digit(n))

