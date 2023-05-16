# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9


    k = int((n*2+0.5)**0.5 - 0.5)
    summands = list(range(1,k))
    n1 = k*(k-1)//2

    summands += [n-n1]
    #print(summands)



    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
