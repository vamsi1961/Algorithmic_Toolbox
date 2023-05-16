# python3

import numpy as np
def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    Matrix = np.zeros((len(first_sequence) + 1, len(second_sequence) + 1, len(third_sequence)+1))
    for i in range(len(first_sequence) + 1):
        for j in range(len(second_sequence) + 1):
            for k in range(len(third_sequence)+1):

                if (i == 0) or (j == 0) or (k ==0):
                    Matrix[i][j][k] = 0

                elif first_sequence[i - 1] == second_sequence[j - 1] == third_sequence[k-1]:
                    Matrix[i][j][k] = Matrix[i - 1][j - 1][k-1] + 1

                else:
                    Matrix[i][j][k] = max(Matrix[i-1][j][k] , Matrix[i][j-1][k] , Matrix[i][j][k-1] , Matrix[i-1][j-1][k] , Matrix[i-1][j][k-1] , Matrix[i][j-1][k-1] , )

                #print(i,j,k)
    #print(Matrix)

    return int(Matrix[-1][-1][-1])


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q


    print(lcs3(a, b, c))
