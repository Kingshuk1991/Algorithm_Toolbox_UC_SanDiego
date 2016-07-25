# Uses python3
import sys

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
		
def lcm(a, b):
    #write your code here
    return int(a/gcd(a,b))*b

input=input("")
token=input.split()
a=int(token[0])
b=int(token[1])
print (lcm(a,b))

