# Uses python3
import sys

def get_optimal_value(capacity,weights,value):
    k=[value[i]/weights[i] for i in range(0,len(value))]
    tot_value=0
    while capacity>0 and len(k)>0:
        ix=k.index(max(k))
        weight_take=min(weights[ix],capacity)
        tot_value+=k[ix]*weight_take
        capacity=capacity-weight_take
        del k[ix]
        del weights[ix]
    return tot_value



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    value = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, value)
    print("{:.10f}".format(opt_value))