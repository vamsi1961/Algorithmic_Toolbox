# python3

import operator

ops ={
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
}

def MinandMax(i,j,m,M,operation):
    minimum = float("+inf")
    maximum = float("-inf")

    for k in range(i,j):
        a = ops[operation[k-1]](M[i][k] , M[k+1][j])
        b = ops[operation[k - 1]](M[i][k], m[k + 1][j])
        c = ops[operation[k - 1]](m[i][k], m[k + 1][j])
        d = ops[operation[k - 1]](m[i][k], M[k + 1][j])
        minimum = min(minimum,a,b,c,d)
        maximum = max(maximum,a,b,c,d)
    return minimum,maximum

def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    n = len(dataset)
    m = [[0]* (n + 1) for _ in range(n + 1)]
    M = [[0]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        m[i][i] = dataset[i-1]
        M[i][i] = dataset[i-1]

    for k in range(1,n):
        for i in range(1,n+1-k):
            j = i+k
            m[i][j] , M[i][j] = MinandMax(i,j,m,M,operation)

    return int(M[1][n])



if __name__ == "__main__":
    expression = input()
    n = len(expression)
    dataset = [int(expression[i]) for i in range(0,n+1,2)]
    operation = [expression[i] for i in range(1, n, 2)]


    print(find_maximum_value(dataset))
