# Uses python3
import sys

def binary_search(a, x):
    low=0
    high=len(a)-1
    return BinarySearch(a,low,high,x)

def BinarySearch(A,low,high,key):
    if high<low:
        return -1
    else:
        mid=int(low+(high-low)/2)
        if A[mid]==key:
            return mid
        elif A[mid]>key:
            return BinarySearch(A,low,mid-1,key)
        else:
            return BinarySearch(A,mid+1,high,key)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
