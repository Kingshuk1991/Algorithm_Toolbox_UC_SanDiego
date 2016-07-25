#python3
def calc_fib(n):
    f=[0,1,1]
    for i in range(1,n+1):
        f[0]=f[1]
        f[1]=f[2]
        f[2]=(f[0]+f[1])
    return f[0]

n = int(input())
print(calc_fib(n))


   