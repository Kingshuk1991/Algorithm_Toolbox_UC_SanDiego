# Uses python3
import sys

def get_fibonaccihuge(n, m):
    # write your code here
    f=[0,1]+[None]*(n-1)
    for i in range(2,n+1):
        f[i]=(f[i-1]+f[i-2])%m
    return f[n]

input = input("")
tokens = input.split()
n = int(tokens[0])
m = int(tokens[1])
print(get_fibonaccihuge(n, m))
