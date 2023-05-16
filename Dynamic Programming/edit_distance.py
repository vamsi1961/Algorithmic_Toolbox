# python3
import numpy as np


def edit_distance(first_string, second_string):
    ln_s1 = len(first_string)
    ln_s2 = len(second_string)

    Matrix = np.zeros((ln_s1 + 1, ln_s2 + 1))
    for i in range(ln_s2 + 1):
        Matrix[0][i] = i

    for j in range(ln_s1 + 1):
        Matrix[j][0] = j

    #print(Matrix)

    for i in range(1, ln_s1 + 1):
        for j in range(1,ln_s2 + 1):
            insertion = Matrix[i][j - 1] + 1
            deletion = Matrix[i-1][j] + 1
            mismatch = Matrix[i - 1][j - 1] + 1
            match = Matrix[i - 1][j - 1]

            if first_string[i - 1] == second_string[j - 1]:
                Matrix[i][j] = min(insertion, deletion, match)

            if first_string[i - 1] != second_string[j - 1]:
                Matrix[i][j] = min(insertion, deletion, mismatch)

    return int(Matrix[-1][-1])


if __name__ == "__main__":
    print(edit_distance(input(), input()))
