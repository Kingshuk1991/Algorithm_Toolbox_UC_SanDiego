# Uses python3
n = int(input())
a = [int(x) for x in input().split()]

assert(len(a) == n)

big=max(a)
i=a.index(big)
del a[i]
big2nd=max(a)
result=big*big2nd



print(result)
