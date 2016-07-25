# Uses python3
import sys

def optimal_summands(n):
    i=0
    summands=[]
    remain=n
    lim_sum=0
    while remain>0 and lim_sum<=n:
        i+=1
        summands.append(i)
        remain=remain-i
        add=int((i*(i+1))/2)
        lim_sum=add+(i+1)
    need=n-add
    summands[-1]=summands[-1]+need
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
