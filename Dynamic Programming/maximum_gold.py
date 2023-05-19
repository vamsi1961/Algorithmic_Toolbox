# python3

from sys import stdin
import numpy as np

def maximum_gold(W, weights):
    assert 1 <= W <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    n = len(weights)
    # make a 2-D Matrix to store capacity and weights
    value = np.zeros((W+1,n+1))
    # columns => no. of items => W
    # rows => no. of weights => n
    for i in range(1,W+1):
        for j in range(1,n+1):
            value[i][j] = value[i][j-1]
            if weights[j-1] <= i:
                value[i][j] = max(value[i][j] , value[i-weights[j-1]][j-1] + weights[j-1])

    return int(value[-1][-1])                # if newly added weight






if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
