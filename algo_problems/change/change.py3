# Uses python3
import sys

def get_change(n):
    n10=n//10
    n=n%10
    n5=n//5
    n=n%5
    return n10+n5+n


n = int(input())
print(get_change(n))
