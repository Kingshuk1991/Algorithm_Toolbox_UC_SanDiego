# Uses python3
import sys

def majority_element(seq, default=None):
    """Find which element in *seq* sequence is in the majority.

    Return *default* if no such element exists.

    Use Moore's linear time constant space majority vote algorithm
    """
    candidate = default
    count = 0
    for e in seq:
        if count != 0:
            count += 1 if candidate == e else -1
        else: # count == 0
            candidate = e
            count = 1

    # check the majority
    return 1 if seq.count(candidate) > len(seq) // 2 else 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
	
print(majority_element(a))
