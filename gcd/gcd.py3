# Uses python3
import sys

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

input = input("")
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])
print(gcd(a, b))
