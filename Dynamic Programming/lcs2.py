# python3
import numpy as np

def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100


    combined = []
    Matrix = np.zeros((len(first_sequence)+1 , len(second_sequence)+1))
    for i in range(len(first_sequence)+1):
        for j in range(len(second_sequence)+1):

            if (i == 0)or (j == 0):
                Matrix[i][j] = 0

            elif first_sequence[i-1] == second_sequence[j-1]:
                Matrix[i][j] = Matrix[i-1][j-1]+1

            else:
                Matrix[i][j] = max(Matrix[i-1][j] , Matrix[i][j-1])

            #print(Matrix)

    return int(Matrix[-1][-1])






if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
